from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'created_date', 'updated_date')
    list_display = ('title','slug','status', 'created_date', 'updated_date')
    search_fields = ('title', 'snippet', 'ingredients', 'instructions')
    summernote_fields = ('content', 'ingredients', 'instructions')