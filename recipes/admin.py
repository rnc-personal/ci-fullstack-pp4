from django.contrib import admin
from .models import Recipe, Comment, HeroSlider, HomepageCTA


# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'created_date', 'updated_date')
    list_display = ('title', 'slug', 'status', 'created_date', 'updated_date')
    search_fields = ('title', 'snippet', 'ingredients', 'instructions')
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'created_date', 'updated_date')
    list_display = ('name', 'body', 'email', 'approved', 'created_date', 'updated_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)

@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'banner_content')
    search_fields = ('recipe__title', 'banner_content')
    list_filter = ('recipe',)

@admin.register(HomepageCTA)
class HomepageCTAAdmin(admin.ModelAdmin):
    list_display = ('cta_header1', 'cta_content1', 'cta_header2', 'cta_content2', 'about_content')
    search_fields = ('cta_header1', 'cta_content1', 'cta_header2', 'cta_content2', 'about_content')


