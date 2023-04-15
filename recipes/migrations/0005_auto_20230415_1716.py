# Generated by Django 3.2.18 on 2023-04-15 17:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0004_auto_20230407_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('bakery', 'Bakery'), ('snacks', 'Snacks'), ('health', 'Health'), ('drinks', 'Drinks'), ('fine-dining', 'Fine Dining')], default='bakery', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='score',
            field=models.ManyToManyField(blank=True, default='bakery', related_name='recipe_score', to=settings.AUTH_USER_MODEL),
        ),
    ]