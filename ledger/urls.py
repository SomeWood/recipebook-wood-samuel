from django.urls import path
from .views import recipe_list, recipe_details, home_page

urlpatterns = [
	path("", home_page, name="home_page"),
	path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:param>", recipe_details, name="recipe_details"),
]

app_name = "ledger"