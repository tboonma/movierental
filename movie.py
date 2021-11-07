from enum import Enum


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


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, price_code: PriceCode):
        # Initialize a new movie.
        if not isinstance(price_code, PriceCode):
            raise TypeError("price_code must be a PriceCode")
        self.title = title
        self.price_code = price_code

    def get_title(self) -> str:
        """Get title for this movie."""
        return self.title

    def get_price_code(self) -> PriceCode:
        """Get price code for this movie."""
        return self.price_code
