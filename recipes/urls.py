from . import views
from django.urls import path
from .views import Custom404View

urlpatterns = [
    path('', views.HomeRecipesView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_listings'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('404/', Custom404View.as_view(), name='404'),
]

# path('newest/', views.HomeRecentRecipesView.as_view(), name='newest_recipes'),