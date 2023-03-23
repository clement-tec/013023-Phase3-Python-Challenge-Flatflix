class Movie:
    
    def __init__(self, title):
        self.title = title
        self.reviews = []
        self.reviewers = []
        
    # title property goes here!
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise ValueError("Titles must be strings greater than 0 characters")
    
    def add_review(self, review, reviewer):
        self.reviews.append(review)
        self.reviewers.append(reviewer)
        
    def average_rating(self):
        if len(self.reviews) > 0:
            return sum(self.reviews) / len(self.reviews)
        else:
            return 0
    
    @classmethod
    def highest_rated(cls, movies):
        highest_rated_movie = None
        highest_rating = 0
        for movie in movies:
            rating = movie.average_rating()
            if rating > highest_rating:
                highest_rating = rating
                highest_rated_movie = movie
        return highest_rated_movie
