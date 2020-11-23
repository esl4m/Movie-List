from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.list_movies, name='list-movies'),
    path('people/', views.list_people, name='list-people'),
]
