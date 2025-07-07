# Class to handle, voting, display winning movie, save users, savemovies, display movies
from .users import User
from .movie import Movie
from utils.file_handler import add_user_to_json, add_movie_to_json, add_vote
import json
import os


class Vote_manager:
    def __init__(self):
        self.users = []
        self.movies = self.load_movies()

    def load_movies(self, MOVIE_FILE = r'C:\Movie Night Planner App\data\movies.json'):
        movies = []
        if os.path.exists(MOVIE_FILE):
            try:
                with open(MOVIE_FILE, 'r') as f:
                    data = json.load(f)
                    for entry in data:
                        movies.append(Movie(
                            entry['title'],
                            entry['release_date'],
                            entry['genre'],
                            vote=entry.get('vote', 0)
                        ))
            except json.JSONDecodeError:
                print("Error reading movies.json")
        return movies

    def add_movie(self, movie):
        if not any(entry.title.lower() == movie.title.lower() for entry in self.movies):
            self.movies.append(movie)
            add_movie_to_json(movie)
        else:
            print(f"{movie.title} already exists in the list.")

    def add_user(self, user):
        if not any(entry.email.lower() == user.email.lower() for entry in self.users):
            self.users.append(user)  
            add_user_to_json(user)
        else:
            print(f"{user.email} already exists in the list.")

    def display_movies(self):
        for i,entry in enumerate(self.movies,1):
            print(f'{i}: {entry.title} - vote: {entry.vote}')

    def show_winner(self):
        winner = max(self.movies, key= lambda m: m.vote)
        print(f'🎉🎉🎉🎉\nTop voted movies is {winner.title} with {winner.vote} votes')


    def vote_movie(self, movie):
        add_vote(movie)

    
        