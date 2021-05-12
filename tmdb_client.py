import requests
import random
import os

api_token = os.environ.get("TMDB_API_TOKEN", "")

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_movies_list(list_type='popular'):
    return call_tmdb_api(f"movie/{list_type}")

def get_poster_url(poster_api_path, size='342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    data = data['results']
    random.shuffle(data)
    return data[:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id, how_many):
    return call_tmdb_api(f"movie/{movie_id}/credits")['cast'][:how_many]


def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")


def search(search_query):
    base_url = "https://api.themoviedb.org/3/"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    endpoint = f"{base_url}search/movie/?query={search_query}"
    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']


def get_airing_today():
    endpoint = "https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']








