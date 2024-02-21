from django.db import models
from django.contrib.auth import get_user_model


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    notes = models.TextField()
    rating = models.IntegerField(default=0)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
