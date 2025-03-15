from django.db import models

# Create your models here.
# Ingredient - name
# Recipe - name
# RecipeIngredient - quantity, ingredient, recipe

class Ingredient(models.Model):
	name = models.CharField(max_length=255)

class Recipe(models.Model):
	name = models.CharField(max_length=255)

class RecipeIngredient(models.Model):
	name = models.CharField(max_length=255)
	ingredient = models.ForeignKey(Ingredient)
	recipe = models.ForeignKey(Recipe)