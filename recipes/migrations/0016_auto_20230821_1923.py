# Generated by Django 3.2.18 on 2023-08-21 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_auto_20230820_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroslider',
            name='link_or_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='heroslider',
            name='slider_type',
            field=models.CharField(choices=[('recipe', 'Recipe'), ('link', 'Link')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='heroslider',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hero_sliders', to='recipes.recipe'),
        ),
    ]
