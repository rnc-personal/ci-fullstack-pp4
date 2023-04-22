from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views import generic, View
from django.http import Http404
from .models import Recipe


# This is for checking which categories are empty / have a recipe attached
# Reference in the readme
def get_categories_with_recipes():
    categories_with_recipes = Recipe.objects.values('category').annotate(recipe_count=Count('category')).filter(recipe_count__gt=0)
    return [item['category'] for item in categories_with_recipes]

class RecipeListView(generic.ListView):
    template_name = 'recipe_list.html'
    paginate_by = 8

    def get(self, request):
        recipes = Recipe.objects.filter(status=1).order_by('-created_date')
        active_categories = get_categories_with_recipes()
    
        context = {
            'recipes': recipes,
            'active_categories': active_categories,
        }

        return render(request, self.template_name, context)


class RecipeByCategoryView(View):
    template_name = 'recipe_list.html'

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category', None)
        active_categories = get_categories_with_recipes()

        if category in dict(Recipe.category.field.choices):
            recipes = Recipe.objects.filter(category=category)
            context = {
                'category': category,
                'recipes': recipes,
                'active_categories': active_categories,
            }
        else:
            raise Http404("Invalid category")

        return render(request, self.template_name, context)


class RecipeByDifficultyView(View):
    template_name = 'recipe_list.html'

    def get(self, request, *args, **kwargs):
        difficulty = request.GET.get('difficulty', None)
        active_categories = get_categories_with_recipes()

        recipes = Recipe.objects.filter(difficulty=difficulty)
        context = {
                'difficulty': difficulty,
                'recipes': recipes,
                'active_categories': active_categories,
            }

        return render(request, self.template_name, context)



class RecipeDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created_date')
        active_categories = get_categories_with_recipes()

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'active_categories': active_categories,
            },
        )

class HomeRecipesView(generic.ListView):
    template_name = 'index.html'
    def get(self, request):
        newest_recipes = Recipe.objects.filter(status=1).order_by('-created_date')[:4]
        trending_recipes = Recipe.objects.all().order_by('-created_date')[:8]

        context = {
            'newest_recipes': newest_recipes,
            'trending_recipes': trending_recipes,
        }

        return render(request, self.template_name, context)

