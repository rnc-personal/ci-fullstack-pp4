from .models import Comment, Recipe
from django import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating',]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'snippet', 'difficulty', 'image', 'instructions', 'ingredients','cooking_time_minutes',] 