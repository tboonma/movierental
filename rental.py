from movie import Movie
from enum import Enum
from datetime import datetime


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior."""

    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2.0 + max((1.5 * (days-2)), 0),
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 + max((1.5 * (days-3)), 0),
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days."""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def frequent_rental_points(self, days: int) -> int:
        """Return the the rental points for a given number of days."""
        frp = self.value["frp"]  # the enum member's frp formula
        return frp(days)

    @staticmethod
    def for_movie(movie: Movie):
        """Get PriceCode for this movie."""
        if movie.year == datetime.now().year:
            return PriceCode.new_release
        if 'Children' in movie.genre:
            return PriceCode.childrens
        return PriceCode.normal


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie: Movie, days_rented: int, price_code: PriceCode):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        if not isinstance(price_code, PriceCode):
            raise TypeError("price_code must be a PriceCode")
        if not isinstance(movie, Movie):
            raise TypeError("movie must be a Movie")
        self.movie: Movie = movie
        self.days_rented: int = days_rented
        self.price_code: PriceCode = price_code

    def get_charge(self) -> float:
        return self.price_code.price(self.days_rented)

    def get_rental_points(self) -> float:
        return self.price_code.frequent_rental_points(self.days_rented)

    def get_title(self) -> str:
        return self.movie.title
