from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
	model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
	model = RecipeImage

class IngredientAdmin(admin.ModelAdmin):
	model = Ingredient

	search_fields = ('name',)

	list_display = ('name',)

	inlines = [RecipeIngredientInline]

class RecipeAdmin(admin.ModelAdmin):
	model = Recipe

	search_fields = ('name',)

	list_display = ('name',)

	inlines = [RecipeIngredientInline, RecipeImageInline]


class RecipeIngredientAdmin(admin.ModelAdmin):
	model = RecipeIngredient

	search_fields = ('recipe', 'ingredient',)

	list_display = ('quantity', 'ingredient', 'recipe',)

	list_filter = ('recipe',)

class RecipeImageAdmin(admin.ModelAdmin):
	model = RecipeImage

	search_fields = ('recipe', 'description',)

	list_display = ('recipe', 'image', 'description',)



admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)