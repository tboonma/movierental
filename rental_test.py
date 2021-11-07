import unittest
from movie import Movie
from rental import Rental, PriceCode


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Mulan", 2021, ['Action', 'Adventure'])
        self.regular_movie = Movie("CitizenFour", 2013, ['Documentary'])
        self.childrens_movie = Movie("Frozen", 2020, ['Action', 'Adventure', 'Children'])

    def test_price_code_attributes(self):
        """
        trivial test to catch refactoring errors or change in API of Movie
        """
        m = Movie("CitizenFour", 2013, ['Documentary'])
        self.assertEqual("CitizenFour", m.get_title())

    def test_invalid_price_code(self):
        """test to catch an Exception for invalid price_code."""
        with self.assertRaises(TypeError):
            movie = Movie("The avengers", 2015, ['Adventure'])
            Rental(movie, 2, 'Action')

    def test_rental_price(self):
        # tests for new movies
        rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
        self.assertEqual(rental.get_charge(), 3.0)
        rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
        self.assertEqual(rental.get_charge(), 15.0)

        # tests for regular movies
        rental = Rental(self.regular_movie, 1, PriceCode.for_movie(self.regular_movie))
        self.assertEqual(rental.get_charge(), 2.0)
        rental = Rental(self.regular_movie, 2, PriceCode.for_movie(self.regular_movie))
        self.assertEqual(rental.get_charge(), 2.0)
        rental = Rental(self.regular_movie, 3, PriceCode.for_movie(self.regular_movie))
        self.assertEqual(rental.get_charge(), 3.5)

        # tests for children movies
        rental = Rental(self.childrens_movie, 1, PriceCode.for_movie(self.childrens_movie))
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.childrens_movie, 2, PriceCode.for_movie(self.childrens_movie))
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.childrens_movie, 3, PriceCode.for_movie(self.childrens_movie))
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.childrens_movie, 4, PriceCode.for_movie(self.childrens_movie))
        self.assertEqual(rental.get_charge(), 3.0)

    def test_rental_points(self):
        # tests for new movies
        rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
        self.assertEqual(rental.get_rental_points(), 5)

        # tests for regular movies
        rental = Rental(self.regular_movie, 1, PriceCode.for_movie(self.regular_movie))
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 2, PriceCode.for_movie(self.regular_movie))
        self.assertEqual(rental.get_rental_points(), 1)

        # tests for children movies
        rental = Rental(self.childrens_movie, 1, PriceCode.for_movie(self.childrens_movie))
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 2, PriceCode.for_movie(self.childrens_movie))
        self.assertEqual(rental.get_rental_points(), 1)
