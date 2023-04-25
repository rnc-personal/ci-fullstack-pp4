from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = (
    ('bakery', 'Bakery'),
    ('snacks', 'Snacks'),
    ('health', 'Health'),
    ('drinks', 'Drinks'),
    ('fine-dining', 'Fine Dining'))


# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes",max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    snippet = models.TextField(max_length=100)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=200, choices=CATEGORY, default='bakery')
    user_recipe_score = models.ManyToManyField(User, related_name='user_recipe_score', blank=True, editable=False)
    ingredients = models.TextField()
    instructions = models.TextField()
    is_featured = models.BooleanField(default=False)
    cooking_time_minutes = models.IntegerField(default=0)
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def average_recipe_score(self):
        return self.user_recipe_score.aggregate()




class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=5)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"Comment: {self.body} by {self.name}"


class HomepageContent(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, related_name='hero_sliders', null=True)
    banner_image = CloudinaryField('banner_image', default='placeholder')
    banner_content = models.CharField(max_length=200, unique=True)
    cta_header1 = models.CharField(max_length=200, unique=True)
    cta_content1 = models.CharField(max_length=200, unique=True)
    cta_header2 = models.CharField(max_length=200, unique=True)
    cta_content2 = models.CharField(max_length=200, unique=True)
    about_content = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('featured_image', default='placeholder')

    class Meta:
        ordering = ['recipe']

    def __str__(self):
        return f'{self.recipe.title} - Slider' if self.recipe else 'No Recipe - Slider'
