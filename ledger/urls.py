from django.urls import path
from .views import recipe_list, recipe_details, home_page, recipe_new

urlpatterns = [
	path("", home_page, name="home_page"),
	path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:param>", recipe_details, name="recipe_details"),
    path("recipe/add", recipe_new, name="recipe_new")
    path("recipe/pk/add_image", recipe_image, name="recipe_image")
]

app_name = "ledger"