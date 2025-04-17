from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.Form):
	name = forms.CharField(label='Recipe Name', max_length=255)
	author = forms.CharField(label='Author Name', max_length=255)