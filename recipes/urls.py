from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeRecipesView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_listings'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]

# path('newest/', views.HomeRecentRecipesView.as_view(), name='newest_recipes'),