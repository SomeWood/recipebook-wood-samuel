from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Ingredient - name
# Recipe - name
# RecipeIngredient - quantity, ingredient, recipe

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	bio = models.CharField(max_length=255)

class Ingredient(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse('recipe', args=[str(self.id)])

class Recipe(models.Model):
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse('recipes/list')


class RecipeIngredient(models.Model):
	quantity = models.TextField()
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')