import unittest
from unittest import TestCase
from price_discount import discount


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_floats(self):
        prices = [10.99, 4.20, 20.11]
        expected_discount = 4.20
        self.assertEqual(expected_discount, discount(prices))

    def test_less_than_three(self):
        prices = [10, 3]
        expected_message = 'You\ve only bought 2 item(s), so you are not eligible for a discount'
        self.assertEqual(expected_message, discount(prices))

    def test_empty_list(self):
        prices = []
        expected_message = 'Enter one or more dollar values'
        self.assertEqual(expected_message, discount(prices))

    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()
