# Generated by Django 3.2.18 on 2023-04-22 11:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0006_recipe_user_recipe_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='user_recipe_score',
            field=models.ManyToManyField(blank=True, editable=False, related_name='user_recipe_score', to=settings.AUTH_USER_MODEL),
        ),
    ]
