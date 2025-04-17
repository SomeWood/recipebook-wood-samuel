from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm

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
    ingredients = Ingredient.objects.all()
    recipeIngredients = RecipeIngredient.objects.all()
    recipeForm = RecipeForm()
    ingredientForm = IngredientForm()
    recipeIngredientForm = RecipeIngredientForm()
    
    if request.method == 'POST':
        if 'aaa' in request.POST:
            recipeForm = RecipeForm(request.POST)
            if recipeForm.is_valid():
                new_recipe = Recipe()
                new_recipe.name = recipeForm.cleaned_data.get('name')
                new_recipe.author = recipeForm.cleaned_data.get('author')
                new_recipe.save()
                return redirect('/recipe/add')
        elif 'bbb' in request.POST:
            ingredientForm = IngredientForm(request.POST)
            if ingredientForm.is_valid():
                new_ingredient = Ingredient()
                new_ingredient.name = ingredientForm.cleaned_data.get('name')
                new_ingredient.save()
                return redirect('/recipe/add')
        elif 'ccc' in request.POST:
            recipeIngredientForm = RecipeIngredientForm(request.POST)
            if recipeIngredientForm.is_valid():
                new_recipeIngredient = RecipeIngredient()
                new_recipeIngredient.quantity = recipeIngredientForm.cleaned_data.get('quantity')
                new_recipeIngredient.ingredient = recipeIngredientForm.cleaned_data.get('ingredient')
                new_recipeIngredient.recipe = recipeIngredientForm.cleaned_data.get('recipe')
                new_recipeIngredient.save()
                return redirect('/recipe/add')

    ctx = {'recipes':recipes, 'ingredients':ingredients,
        'recipeIngredients':recipeIngredients, 'recipeForm':recipeForm, 
        'ingredientForm':ingredientForm, 'recipeIngredientForm':recipeIngredientForm
    }
    
    return render(request, 'recipe_new.html', ctx)

@login_required
def recipe_image(request, param):
    recipe = Recipe.objects.get(id=param)

    return render(request, 'recipe_image.html', {})

def home_page(request):
    return redirect('/accounts/login')