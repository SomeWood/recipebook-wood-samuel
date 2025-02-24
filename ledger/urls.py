from django.urls import path
from .views import home
from .views import list
from .views import recipes

urlpatterns = [
	path("", home, name="home"),
	path("recipes/list", list, name="list"),
    path("recipe/<int:number>", recipes, name="recipes"),
]

app_name = "ledger"