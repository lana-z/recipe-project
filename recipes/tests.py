from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Recipe


class RecipeTests(APTestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_recipe = Recipe.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_recipe.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_recipes_model(self):
        recipe = Recipe.objects.get(id=1)
        actual_owner = str(recipe.owner)
        actual_name = str(recipe.name)
        actual_description = str(recipe.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_recipe_list(self):
        url = reverse("recipe_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        recipes = response.data
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0]["name"], "rake")

    def test_get_recipe_by_id(self):
        url = reverse("recipe_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        recipe = response.data
        self.assertEqual(recipe["name"], "rake")

    def test_create_recipe(self):
        url = reverse("recipe_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        recipes = Recipe.objects.all()
        self.assertEqual(len(recipes), 2)
        self.assertEqual(Recipe.objects.get(id=2).name, "spoon")

    def test_update_recipe(self):
        url = reverse("recipe_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.name, data["name"])
        self.assertEqual(recipe.owner.id, data["owner"])
        self.assertEqual(recipe.description, data["description"])

    def test_delete_recipe(self):
        url = reverse("recipe_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        recipes = Recipe.objects.all()
        self.assertEqual(len(recipes), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("recipe_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
