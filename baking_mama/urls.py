"""baking_mama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipes import views
from .views import page_not_found_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'), name='recipe_urls'),
    path('category/', views.RecipeByCategoryView.as_view(), name='category_view'),
    path('difficulty/', views.RecipeByDifficultyView.as_view(), name='difficulty_view'),
    path('submit/', views.RecipeSubmissionView.as_view(), name='recipe_submission'),
    path('confirm/', views.SubmissionConfirmView.as_view(), name='submission_confirm'),
    path('time/', views.RecipeByTimeView.as_view(), name='time_view'),
    path('rating/', views.TrendingRecipesListView.as_view(), name='rating_view'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    
]


handler404 = "baking_mama.views.page_not_found_view"