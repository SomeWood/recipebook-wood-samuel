from django.urls import path
from .views import home
from .views import recipe_list
from .views import recipe_details

urlpatterns = [
	path("", home, name="home"),
	path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:number>", recipe_details, name="recipe_details"),
]

app_name = "ledger"