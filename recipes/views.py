from django.shortcuts import render
from django.views import generic, View
from .models import Recipe

# Create your views here.


class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetailView(View):
    def get(self, slug, *args, **kwargs):
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




