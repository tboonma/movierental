from movie import Movie


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

    def __init__(self, movie: Movie, days_rented: int):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie: Movie = movie
        self.days_rented: int = days_rented

    def get_charge(self) -> float:
        return self.movie.get_price_code().price(self.days_rented)

    def get_rental_points(self) -> float:
        return self.movie.get_price_code().\
            frequent_rental_points(self.days_rented)

    def get_title(self) -> str:
        return self.movie.title
