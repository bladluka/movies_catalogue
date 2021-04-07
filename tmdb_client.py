import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNWMyMTZmODZhMDZjY2JkYWFjZWY0MWIxYzEyNzJkMiIsInN1YiI6IjYwNjk2OTUwMGMzZWM4MDA2ZTdmYmI2YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8YbcrBZ9lclwMhTIrTcwFor_futjDkpcMV3hTsDSANw"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size='342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data['results'][:how_many]
