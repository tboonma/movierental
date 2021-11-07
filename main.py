# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental, PriceCode
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", 2021, ['Drama', 'Thriller']),
        Movie("CitizenFour", 2020, ['Documentary']),
        Movie("Frozen", 2019, ['Action', 'Adventure', 'Children']),
        Movie("El Camino", 2021, ['Drama']),
        Movie("Particle Fever", 2020, ['Thriller'])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, PriceCode.for_movie(movie)))
        days += 1
    print(customer.statement())
