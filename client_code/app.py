
import requests
movie_name =  requests.get("http://10.20.24.54:5000/get-movie-name")
name_of_movie = movie_name.json()['name']
print(movie_name.json())

