from django import forms
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeForm(forms.Form):
	name = forms.CharField(label='Recipe Name', max_length=255)
	author = forms.CharField(label='Author Name', max_length=255)

class IngredientForm(forms.Form):
	name = forms.CharField(label='Ingredient Name', max_length=255)

class RecipeIngredientForm(forms.Form):
	quantity = forms.CharField(label='Quantity', max_length=255)
	ingredient = forms.ModelChoiceField(label='Ingredient Name', queryset=Ingredient.objects.all())
	recipe = forms.ModelChoiceField(label='Recipe Name', queryset=Recipe.objects.all())

class RecipeImageForm(forms.Form):
	image = forms.ImageField(label='Image')
	description = forms.CharField(label='Description', max_length=255)