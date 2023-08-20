from . import views
from django.urls import path, re_path
from .views import EditRecipeView, DeleteRecipeView

urlpatterns = [
    path('', views.HomeRecipesView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_listings'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('edit/<slug:slug>/', views.EditRecipeView.as_view(), name='edit_recipe'),
    path('delete/<slug:slug>/', DeleteRecipeView.as_view(), name='delete_recipe'),
]

handler404 = "baking_mama.views.page_not_found_view"
