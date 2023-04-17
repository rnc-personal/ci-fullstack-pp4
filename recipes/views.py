from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class RecipeListView(generic.ListView):
    template_name = 'recipe_list.html'
    paginate_by = 6

    def get(self, request):
        newest_recipes_list = Recipe.objects.filter(status=1).order_by('-created_date')
        trending_recipes_list = Recipe.objects.all().order_by('-created_date')

        context = {
            'newest_recipes_list': newest_recipes_list,
            'trending_recipes_list': trending_recipes_list,
        }

        return render(request, self.template_name, context)



class RecipeDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created_date')

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments
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

