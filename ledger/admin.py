from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
	model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
	model = Ingredient

	search_fields = ('name',)

	list_display = ('name',)

	inlines = [RecipeIngredientInline,]

class RecipeAdmin(admin.ModelAdmin):
	model = Recipe

	search_fields = ('name',)

	list_display = ('name', 'image')

	inlines = [RecipeIngredientInline,]


class RecipeIngredientAdmin(admin.ModelAdmin):
	model = RecipeIngredient

	search_fields = ('recipe', 'ingredient',)

	list_display = ('quantity', 'ingredient', 'recipe',)

	list_filter = ('recipe',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)