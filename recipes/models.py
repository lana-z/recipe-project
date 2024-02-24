from django.db import models
from django.contrib.auth import get_user_model


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    notes = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
