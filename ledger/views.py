from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.

def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())

def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipe_list.html', {'recipes':recipes})


def recipe_details(request, param):
    recipe = Recipe.objects.get(id=param)

    return render(request, 'recipe_details.html', {'recipe':recipe})