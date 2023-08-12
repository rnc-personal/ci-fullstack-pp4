from . import views
from django.urls import path, re_path



urlpatterns = [
    path('', views.HomeRecipesView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_listings'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('submit/', views.RecipeSubmissionView.as_view(), name='recipe_submission'),
    
]

handler404 = "baking_mama.views.page_not_found_view"
