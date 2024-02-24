from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__' # ('name', 'owner', 'notes', 'rating', 'created_at', 'updated_at')