from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    purchaser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField(max_length=256)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('Recipe_detail', args=[str(self.id)])