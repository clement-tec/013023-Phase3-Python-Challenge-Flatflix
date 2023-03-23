from.viewer import Viewer
from.movie import Movie

class Review:
    def __init__(self, viewer, movie, rating):
        if not isinstance(viewer, Viewer):
            raise TypeError("viewer must be a Viewer instance")
        if not isinstance(movie, Movie):
            raise TypeError("movie must be a Movie instance")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("rating must be an integer between 1 and 5, inclusive")
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        self.viewer.add_review(self)
        self.movie.add_review(self)

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, value):
        if not isinstance(value, Viewer):
            raise TypeError("viewer must be a Viewer instance")
        self._viewer = value

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, value):
        if not isinstance(value, Movie):
            raise TypeError("movie must be a Movie instance")
        self._movie = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("rating must be an integer between 1 and 5, inclusive")
        self._rating = value
