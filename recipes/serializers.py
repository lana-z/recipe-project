from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__' # ('name', 'added_by', 'notes', 'rating', 'link', 'created_at', 'updated_at')