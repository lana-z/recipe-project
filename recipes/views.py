from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeListView(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

