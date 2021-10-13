import unittest

from movie import Movie, PriceCode
from rental import Rental


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Mulan", PriceCode.new_release)
        self.regular_movie = Movie("CitizenFour", PriceCode.normal)
        self.childrens_movie = Movie("Frozen", PriceCode.childrens)

    def test_price_code_attributes(self):
        """
        trivial test to catch refactoring errors or change in API of Movie
        """
        m = Movie("CitizenFour", PriceCode.normal)
        self.assertEqual("CitizenFour", str(m))
        self.assertEqual(PriceCode.normal, m.get_price_code())

    def test_invalid_price_code(self):
        """test to catch an Exception for invalid price_code."""
        with self.assertRaises(TypeError):
            Movie("The avengers", 2)

    def test_rental_price(self):
        # tests for new movies
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        # tests for regular movies
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)

        # tests for children movies
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)

    def test_rental_points(self):
        # tests for new movies
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_renter_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_renter_points(), 5)

        # tests for regular movies
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_renter_points(), 1)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_renter_points(), 1)

        # tests for children movies
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_renter_points(), 1)
        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_renter_points(), 1)
