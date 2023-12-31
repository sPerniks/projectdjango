# Generated by Django 4.2.6 on 2023-10-16 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_category_slug_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації', 'verbose_name_plural': 'Категорії для публікацій'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default-value-here', verbose_name='Слаг'),
        ),
    ]
