# Building class on movie creation

class Movie:
    def __init__(self, title, release_date, genre, vote = 0):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.vote = vote
     
    def up_vote(self):
        self.vote +=1
        return f"You have voted {self.title}, now has {self.vote} votes"

    def __str__(self):
        return f"{self.title} has been added"

