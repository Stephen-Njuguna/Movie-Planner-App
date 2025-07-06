# File handles, adding and updating json files
import json
import os
import sys
sys.path.append(r'C:\Movie Night Planner App')

from models.users import User
from models.movie import Movie
# from models.vote_manager import Vote_manager

#adding users to json file

def add_user_to_json(user, file_path = r'C:\Movie Night Planner App\data\users.json'):
    entry = {
        'name':user.name,
        'email':user.email,
    }
    users_data = []
    if not os.path.exists(file_path):
        print('debug: check on users path')

    if os.path.exists(file_path):
        try:
            with open(file_path,'r') as f:
                users_data = json.load(f)
        except json.JSONDecodeError:
            users_data =[]

        find_user = any(user.email.lower() == s['email'].lower() for s in users_data)

        if find_user:
            print(f'{user.name} already exist!')
        else:
            users_data.append(entry)

        with open(file_path, 'w') as f:
            json.dump(users_data, f, indent=4)

def add_movie_to_json(movie, file_path= r'C:\Movie Night Planner App\data\movies.json'):
    movies = []

    entry = {
        'title':movie.title,
        'release_date':movie.release_date,
        'genre':movie.genre,
        'vote':movie.vote
    };

    if not os.path.exists(file_path):
        print(f'check on file path {file_path}')

    if os.path.exists(file_path):
        try:
            with open(file_path) as mf:
                movies =json.load(mf)
        except json.JSONDecodeError:
            movies = []

        find_movie = any(movie.title.lower() == m['title'].lower() for m in movies)

        if find_movie:
            print(f'{movie.title.title()} already exists.')
        else:
            movies.append(entry)
            print(f'{movie.title.title()} has been added')

        with open(file_path, 'w') as mf:
            json.dump(movies, mf, indent=4)


def add_vote(movie, file_path =r'C:\Movie Night Planner App\data\movies.json'):
    movies = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                movies = json.load(f)
        except json.JSONDecodeError:
            movies = []

    for entry in movies:
        if entry['title'].lower() == movie.title.lower():
            entry['vote'] = entry.get('vote', 0)+1
        break

    with open(file_path, "w") as f:
        json.dump(movies, f, indent=4)
