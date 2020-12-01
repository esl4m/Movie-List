from collections import defaultdict
from django.core.cache import cache
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
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
    if movie_people:
        cache.set("movie-people", movie_people, 60)  # set the movie-people in cache for 1 min
    return movie_people

@cache_page(60 * 1)  # 1 min cache & getting the cache from settings by default no changes.
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
            
            cache.set("movies", films, 60)  # set the movies in cache for 1 min

        # response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        raise Http404("No Movies")
    
    return render(request, "list_movies.html", {"movies": films} )


def list_people(request):
    """ Function to list all people from the endpoint /people """
    try:
        response = requests.get(base_url + "people",  timeout=5)
        people = response.json()
        if people:
            cache.set("list-people", people, 60)  # set the movie-people in cache for 1 min
            
    except requests.exceptions.HTTPError as err:
        raise Http404("No People to display")
    return render(request, 'list_people.html', {'people': people} )
