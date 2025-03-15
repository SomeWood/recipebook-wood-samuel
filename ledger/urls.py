from django.urls import path
from .views import recipe_list
from .views import recipe_details

urlpatterns = [
	path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:param>", recipe_details, name="recipe_details"),
]

app_name = "ledger"