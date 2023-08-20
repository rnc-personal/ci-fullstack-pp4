from .models import Comment, Recipe
from django import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating',]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'snippet',
            'difficulty',
            'image',
            'ingredients_1',
            'ingredients_2',
            'ingredients_3',
            'ingredients_4',
            'ingredients_5',
            'ingredients_6',
            'ingredients_7',
            'ingredients_8',
            'instructions_1',
            'instructions_2',
            'instructions_3',
            'instructions_4',
            'instructions_5',
            'instructions_6',
            'instructions_7',
            'instructions_8',
            'cooking_time_minutes',
            ] 