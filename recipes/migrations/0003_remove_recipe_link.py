# Generated by Django 5.0.2 on 2024-02-21 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_purchaser_recipe_added_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='link',
        ),
    ]