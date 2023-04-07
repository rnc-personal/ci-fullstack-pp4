from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
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
    score = models.IntegerField(default=0)
    content = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def recipe_score(self):
        return self.score.count()

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment: {self.body} by {self.name}"