from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Avg, Q
from django.views import generic, View
from django.views.generic import ListView
from django.http import Http404, HttpResponseNotFound
from django.db import models
from django.utils.text import slugify
from django.contrib import messages
from .models import Recipe, HeroSlider, HomepageCTA
from .forms import CommentForm, RecipeForm


class RecipeListView(generic.ListView):
    template_name = 'recipe_list.html'
    paginate_by = 8
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = Recipe.objects.filter(status=1).order_by('-created_date')
        return queryset


class RecipeByCategoryView(View):
    template_name = 'recipe_list.html'

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category', None)

        if category in dict(Recipe.category.field.choices):
            recipes = Recipe.objects.filter(category=category, status=1)
            context = {
                'category': category,
                'recipes': recipes,
            }
        else:
            raise Http404("Invalid category")

        return render(request, self.template_name, context)

class RecipeByTimeView(View):
    template_name = 'recipe_list.html'

    def get(self, request, *args, **kwargs):
        time_lt = request.GET.get('cooking_time_minutes_lt', None)
        time_gt = request.GET.get('cooking_time_minutes_gt', None)

        recipes = Recipe.objects.filter(status=1)

        if time_lt is not None:
            recipes = recipes.filter(cooking_time_minutes__lt=time_lt)

        if time_gt is not None:
            recipes = recipes.filter(cooking_time_minutes__gt=time_gt)

        context = {
            'recipes': recipes,
        }

        return render(request, self.template_name, context)


class RecipeByDifficultyView(View):
    template_name = 'recipe_list.html'

    def get(self, request, *args, **kwargs):
        difficulty = request.GET.get('difficulty', None)
        easy_recipes = Recipe.objects.filter(difficulty=1, status=1).order_by('-created_date')
        novice_recipes = Recipe.objects.filter(difficulty=2, status=1).order_by('-created_date')
        intermediate_recipes = Recipe.objects.filter(difficulty=3, status=1).order_by('-created_date')
        tricky_recipes = Recipe.objects.filter(difficulty=4, status=1).order_by('-created_date')
        expert_recipes = Recipe.objects.filter(difficulty=5, status=1).order_by('-created_date')

        recipes = Recipe.objects.filter(difficulty=difficulty, status=1)
        context = {
                'difficulty': difficulty,
                'recipes': recipes,
                'easy_recipes': easy_recipes,
                'novice_recipes': novice_recipes,
                'intermediate_recipes': intermediate_recipes,
                'tricky_recipes': tricky_recipes,
                'expert_recipes': expert_recipes,
            }

        return render(request, self.template_name, context)


class RecipeDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created_date')
        avg_rating = recipe.comments.filter(approved=True).aggregate(Avg('rating'))['rating__avg'] or 0

        is_author = False
        if request.user.is_authenticated:
            is_author = recipe.author == request.user

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm(),
                'avg_rating': avg_rating,
                'is_author': is_author,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created_date')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
                
            },
        )

class RecipeSubmissionView(View):
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'recipe_submission.html',
            {
                'recipe_form': RecipeForm(),
            },
        )
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe_form.instance.email = request.user.email
                recipe_form.instance.name = request.user.username
                recipe = recipe_form.save(commit=False)
                recipe.slug = slugify(recipe.title)
                recipe.author = request.user
                recipe.save()
                return redirect('submission_confirm')
        else:
            recipe_form = RecipeForm()
    
        context = {
            'form': recipe_form,
            'submitted': True,
        }
        return render(
            request,
            'recipe_submission.html',
            context
            )

class SubmissionConfirmView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
          'submission_confirm.html',
            {
              'submitted': True,
            },
        )


class EditRecipeView(View):
    def get(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug, author=request.user)

        recipe_form = RecipeForm(instance=recipe)
        return render(
            request,
            'edit_recipe.html',
            {
                'recipe_form': recipe_form,
                'recipe': recipe,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug, author=request.user)

        recipe_form = RecipeForm(request.POST, instance=recipe)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('recipe_detail', slug=slug)

        return render(
            request,
            'edit_recipe.html',
            {
                'recipe_form': recipe_form,
                'recipe': recipe,
            }
        )


class DeleteRecipeView(View):
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.author != request.user:
            messages.error(request, "You are not authorized to delete this recipe.")
            return redirect('recipe_detail', slug=slug)

        recipe.delete()
        messages.success(request, "Recipe Deleted Successfully")
        return redirect('home')


# "Generic" Views for Site Content / Non User Created Content

class HomeRecipesView(generic.ListView):
    template_name = 'index.html'
    def get(self, request):
        newest_recipes = Recipe.objects.filter(status=1).order_by('-created_date')[:4]
        trending_recipes = Recipe.objects.filter(status=1).order_by('-created_date')[:8]
        homepage_sliders = HeroSlider.objects.all()
        homepage_content = HomepageCTA.objects.all()

        context = {
            'newest_recipes': newest_recipes,
            'trending_recipes': trending_recipes,
            'homepage_sliders': homepage_sliders,
            'homepage_content': homepage_content,
        }

        return render(request, self.template_name, context)

class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.model.objects.filter(
                Q(title__icontains=query) & Q(status=1))
        else:
            return self.model.objects.none()


class TrendingRecipesListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 8

    def get_queryset(self):
        min_score = self.request.GET.get('min_score', 0)

        queryset = super().get_queryset().annotate(
            average_score=Avg('comments__rating', filter=models.Q(comments__approved=True))
        ).filter(
            average_score__gte=min_score,
            status=1
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        active_recipes = Recipe.objects.filter(status=1)
        context['rating_counts'] = {
            'gte_3': Recipe.objects.annotate(avg_rating=Avg('comments__rating', filter=models.Q(comments__approved=True))).filter(avg_rating__gte=3).count(),
            'gte_5': Recipe.objects.annotate(avg_rating=Avg('comments__rating', filter=models.Q(comments__approved=True))).filter(avg_rating__gte=5).count(),
            'gte_7': Recipe.objects.annotate(avg_rating=Avg('comments__rating', filter=models.Q(comments__approved=True))).filter(avg_rating__gte=7).count(),
            'gte_9': Recipe.objects.annotate(avg_rating=Avg('comments__rating', filter=models.Q(comments__approved=True))).filter(avg_rating__gte=9).count(),
            'eq_10': Recipe.objects.annotate(avg_rating=Avg('comments__rating', filter=models.Q(comments__approved=True))).filter(avg_rating=10).count(),
        }

        return context

class Custom404View(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)