from collections import defaultdict
from django.core.cache import cache
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
import requests, json


base_url = "https://ghibliapi.herokuapp.com/"

def movie_people():
    """ function to get people in movie """
    response = requests.get(base_url + "people",  timeout=5)
    people = response.json()
    movie_people = defaultdict(list)

    if response:
        # in-case response is not empty, 
        # append person name to the array in movie_people dict
        for person in people:
            for film in person.get("films"):
                film_id = film.split("/")[-1]
                movie_people[film_id].append(person.get("name"))
    movie_people = dict(movie_people)
    return movie_people


def list_movies(request):
    """
    Function to list all movies with people names. 
    since the people field is broken, this fucntion calls movie_people to get people from another endpoint.
    """
    try:
        films = cache.get('movies')
        if not films:
            response = requests.get(base_url + "films",  timeout=5)
            films = response.json()
            people = movie_people()
            for film in films:
                film["people"] = people.get(film.get("id"), [])
            cache.set("movies", films, 60)  # set the films in cache key:"movies" --> for 1 min

    except requests.exceptions.HTTPError as err:
        raise Http404("No Movies")
    
    return render(request, "list_movies.html", {"movies": films} )


def list_people(request):
    """ Function to list all people from the endpoint /people """
    try:
        people = cache.get('list-people')
        if not people:
            response = requests.get(base_url + "people",  timeout=5)
            people = response.json()
            cache.set("list-people", people, 60)  # set the people in cache
            
    except requests.exceptions.HTTPError as err:
        raise Http404("No People to display")
    return render(request, 'list_people.html', {'people': people} )
