from django.urls import path
from .views import home
from .views import list

urlpatterns = [
	path("", home, name="home"),
	path("recipes/list", list, name="list"),
    path("recipe/1", home, name="home"),
    path("recipe/2", home, name="home"),
]