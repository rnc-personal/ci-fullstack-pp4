# Generated by Django 3.2.18 on 2023-04-25 20:03

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_homepagecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='banner_image')),
                ('banner_content', models.CharField(max_length=200, unique=True)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hero_sliders', to='recipes.recipe')),
            ],
            options={
                'ordering': ['recipe'],
            },
        ),
        migrations.CreateModel(
            name='HomepageCTA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cta_header1', models.CharField(max_length=200, unique=True)),
                ('cta_content1', models.CharField(max_length=200, unique=True)),
                ('cta_header2', models.CharField(max_length=200, unique=True)),
                ('cta_content2', models.CharField(max_length=200, unique=True)),
                ('about_content', models.CharField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='featured_image')),
            ],
            options={
                'verbose_name': 'Homepage CTA',
                'verbose_name_plural': 'Homepage CTAs',
            },
        ),
        migrations.DeleteModel(
            name='HomepageContent',
        ),
    ]
