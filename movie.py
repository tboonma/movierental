from collections.abc import Collection
import csv


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: int, genre: Collection[str]):
        # Initialize a new movie.
        self.__title: str = title
        self.__year: int = year
        self.__genre: Collection[str] = genre

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def genre(self):
        return self.__genre

    def get_title(self) -> str:
        """Get title for this movie."""
        return self.title

    def is_genre(self, genre: str) -> bool:
        """Check whether genre is matched.

        Args:
            genre: genre to check does it match with any of movie genre.

        Returns
            True if the string parameter matches one of the movie’s genre.
        """
        return genre in self.genre


class MovieCatalog:

    def __init__(self):
        self.movies: dict[str, Movie] = {}

    def get_movie(self, movie_name: str) -> Movie:
        if movie_name not in self.movies.keys():
            self.__load_movie()
        return self.movies[movie_name]

    def __load_movie(self):
        movie_file = open('movies.csv', "r")
        movie_list = csv.DictReader(movie_file)
        for movie in movie_list:
            self.movies.update({movie['title']: Movie(movie['title'], movie['year'], movie['genres'].split('|'))})
