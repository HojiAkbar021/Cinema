from django.urls import path
from . import views
from movies.views import movie_create

urlpatterns = [
    path('', views.settings, name = "index"),
    path('movie/create', movie_create, name="movie_create" )
]