from django.urls import path
from .views import home
from .views import list
from .views import recipes

urlpatterns = [
	path("", home, name="home"),
	path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:number>", recipe_details, name="recipe_details"),
]

app_name = "ledger"