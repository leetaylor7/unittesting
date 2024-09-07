"""
Imports required modules functions
"""
import unittest
from tested_functions import adder, divider


class TestAdder(unittest.TestCase):
    """
    This class does the unit testing
    """
    def test_adds_three_and_five_correctly(self):
        """
        This method checks adding functionality
        """
        self.assertEqual(adder(3, 5), 8)

    def test_adds_negative_three_and_negative_five_correctly(self):
        """
        This method checks adding negative numbers functionality
        """
        self.assertEqual(adder(-3, -5), -8)

    def test_adds_five_to_zero_correctly(self):
        """
        This method checks adding to zero functionality
        """
        self.assertEqual(adder(0, 5), 5)

    def test_adds_one_two_and_three_integers_correctly(self):
        """
        This method checks adding to more than 2 integers functionality
        """
        self.assertEqual(adder(1, 2, 3), 6)

    def test_adds_forty_integers_correctly(self):
        """
        This method checks adding a longer list capabilities
        """
        sample_list = range(0, 40, 1)
        self.assertEqual(adder(*sample_list), 780)

    def test_raises_an_exception_when_given_one_argument(self):
        """
        This method checks for missing arguments
        """
        self.assertRaises(TypeError, adder(10))

    def test_raises_an_exception_on_string_arguments(self):
        """
        This method checks for strings arguments
        """
        self.assertRaises(TypeError, adder(3, "12"))

class TestDivider(unittest.TestCase):
    """Requirements to test:
    - Returns non-integer results (does not floor divide)
    - Raises ValueError if too many or too few arguments provided (division is binary)
    - Raises TypeError if non-integer arguments provided
    - Raises ValueError if attempting to divide by 0
    - Handles arbitrarily large integer dividends/divisors
    """
    def test_divides_two_integers_correctly(self):
        """
        Checks division functionality
        """
        self.assertEqual(divider(10, 2), 5)

    def test_raises_an_exception_when_given_one_argument(self):
        """
        Checks to make sure more than one argument is given
        """
        self.assertRaises(TypeError, divider(10))

    def test_raises_an_exception_on_string_arguments(self):
        """
        Checks to make sure no strings are given as arguments
        """
        self.assertRaises(TypeError, divider(3, "12"))

    def test_raises_an_exception_on_dividing_by_zero(self):
        """
        Checks to make sure this does not divide by zero
        """
        self.assertRaises(ValueError, divider(3, 0))

    def test_large_integer_dividends_and_divisors(self):
        """
        Test with large dividend and divisor
        """
        large_dividend = 10**18
        large_divisor = 10**9
        result = divider(large_dividend, large_divisor)
        self.assertEqual(result, 10**9)

# Run the tests
if __name__ == '__main__':
    unittest.main()
    