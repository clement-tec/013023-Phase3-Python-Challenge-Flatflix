class Viewer:
    
    def __init__(self, username):
        self.username = username

        self.reviewed_movies = []
        self.reviews = []


    # username property goes here!
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if 6 <= len(username) <= 16 :
            self._username = username
        else:
            raise ValueError("Username must be between 6 and 16 characters long")

    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass