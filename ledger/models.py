from django.db import models

# Create your models here.
# Ingredient - name
# Recipe - name
# RecipeIngredient - quantity, ingredient, recipe

class Ingredient(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse('recipe', args=[str(self.id)])

class Recipe(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse('recipes/list')


class RecipeIngredient(models.Model):
	quantity = models.TextField()
	ingredient = models.ForeignKey(Ingredient)
	recipe = models.ForeignKey(Recipe)