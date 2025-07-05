from models.movie import Movie
from models.users import User
from models.vote_manager import Vote_manager
from utils.file_handler import add_user_to_json, add_movie_to_json
import sys
sys.path.append(r'C:\Movie Night Planner App')

def main():

    movie1 = Movie("Head of States", "2025", "Action&Thriller")

    print(movie1)  
    # print(movie1.up_vote())  
 
    print("All movies in collection:", movie1.movies) 
    print(f"Current vote count for '{movie1.title}':", movie1.vote)

    u = User
    user1 = u("John", "john.doe@gmail.com")
    # print(user1)
    # print(f'-----------printing user added----')
    # added_user = u.create_user((user1))
    # print(added_user)

    add_user_to_json(user1)
    add_movie_to_json(movie1)

if __name__ == "__main__":
    main()