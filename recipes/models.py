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
    snippet = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=200, choices=CATEGORY, default='bakery')
    # score = models.ManyToManyField(User, through='RecipeScore', related_name='recipe_score', blank=True, editable=False)
    content = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    # Reference this in Readme as had to look this up.
    def save(self, *args, **kwargs):
            if self.is_featured:
                # check if there are already 2 featured recipes
                if Recipe.objects.filter(is_featured=True).count() == 2:
                    raise ValidationError("Only 2 recipes can be featured at a time.")
            super(Recipe, self).save(*args, **kwargs)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"Comment: {self.body} by {self.name}"