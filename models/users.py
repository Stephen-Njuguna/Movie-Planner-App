# Class to add users of the app either to vote or add movies

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.users = []

    
    def __str__(self):
        return f"{self.name} has been added."