from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm

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
    recipeIngredients = RecipeIngredient.objects.all()
    recipeForm = RecipeForm()
    ctx = {'recipes':recipes, 'recipeIngredients':recipeIngredients, 
        'recipeForm':recipeForm
    }
    
    return render(request, 'recipe_new.html', ctx)

def home_page(request):
    return redirect('/accounts/login')