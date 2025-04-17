from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipe_list.html', {'recipes':recipes})

@login_required
def recipe_details(request, param):
    recipe = Recipe.objects.get(id=param)

    return render(request, 'recipe_details.html', {'recipe':recipe})

@login_required
def recipe_new(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipe_list.html', {'recipes':recipes})

def home_page(request):
    return redirect('/accounts/login')