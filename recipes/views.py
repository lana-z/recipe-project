from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from django.urls import reverse_lazy

class RecipeListView(ListView):
    template_name = 'recipe_list.html'
    model = Recipe
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    template_name = 'recipe_detail.html'
    model = Recipe

class RecipeCreateView(CreateView):
    template_name = 'recipe_create.html'
    model = Recipe
    fields = 'name', 'purchaser', 'description', 'rating'
    success_url = reverse_lazy('recipe_list')

class RecipeUpdateView(UpdateView):
    template_name = 'recipe_update.html'
    model = Recipe
    fields = '__all__'

class RecipeDeleteView(DeleteView):
    template_name = 'recipe_delete.html'
    model = Recipe
    success_url = reverse_lazy('recipe_list')
