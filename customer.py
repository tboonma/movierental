from rental import Rental
from movie import Movie
from rental import PriceCode


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """
    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name: str = name
        self.rentals: list[Rental] = []

    def add_rental(self, rental: Rental):
        """Add rental to this customer.

        Args:
            rental: the rental that customer ordered.
        """
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self) -> str:
        """Get this customer's name.

        Returns:
            customer's name as a string.
        """
        return self.name

    def compute_rental_points(self) -> int:
        """Get total rental points for this customer purchase.

        Returns:
            total rental points as an integer.
        """
        rental_points = 0
        for rental in self.rentals:
            rental_points += rental.get_rental_points()
        return rental_points

    def compute_total_charge(self) -> float:
        """Get total charge for this customer's purchase.

        Returns:
            total charge as a float.
        """
        amount = 0
        for rental in self.rentals:
            amount += rental.get_charge()
        return amount

    def statement(self) -> str:
        """Print all the rentals in current period,
        along with total charges and reward points.

        Returns:
            the statement as a string.
        """
        total_amount = self.compute_total_charge()
        frequent_renter_points = self.compute_rental_points()

        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            #  add detail line to statement
            statement += fmt.format(str(rental.get_title()),
                                    rental.days_rented,
                                    rental.get_charge())

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(
            frequent_renter_points)

        return statement

    def __str__(self):
        return self.name


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", 2020, ['Documentary'])
    customer.add_rental(Rental(movie, 2, PriceCode.for_movie(movie)))
    movie = Movie("CitizenFour", 2021, ['Drama'])
    customer.add_rental(Rental(movie, 3, PriceCode.for_movie(movie)))
    print(customer.statement())
