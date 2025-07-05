# Class to handle, voting, display winning movie, save users, savemovies, display movies
from .users import User
from .movie import Movie
from utils.file_handler import add_user_to_json, add_movie_to_json



class Vote_manager:
    def __init__(self):
        self.users = []
        self.movies = []

    def add_movie(self, movie):
        