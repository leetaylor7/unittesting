import unittest
from tested_functions import adder, divider


class TestAdder(unittest.TestCase):
    def test_adds_two_integers_correctly(self):
        self.assertEqual(adder(3, 5), 8)

    def test_adds_negative_numbers_correctly(self):
        self.assertEqual(adder(-3, -5), -8)

    def test_adds_numbers_to_zero_correctly(self):
        self.assertEqual(adder(0, 5), 5)

    def test_adds_three_integers_correctly(self):
        self.assertEqual(adder(1, 2, 3), 6)

    def test_adds_forty_integers_correctly(self):
        sample_list = []
        
        for i in range(0, 40, 1):
            sample_list.append(1)
        self.assertEqual(adder(*sample_list), 40)

    def test_raises_an_exception_when_given_one_argument(self):
        self.assertRaises(TypeError, adder(10))

    def test_raises_an_exception_on_string_arguments(self):
        self.assertRaises(TypeError, adder(3,"12"))


class TestDivider(unittest.TestCase):
    """Requirements to test:
    
        - Returns non-integer results (does not floor divide)
        - Raises ValueError if too many or too few arguments provided (division is binary)
        - Raises TypeError if non-integer arguments provided
        - Raises ValueError if attempting to divide by 0 (treating the error as a bad argument issue, not a math issue)
        - Handles arbitrarily large integer dividends/divisors
        - Can be called multiple times in succession accurately (divider(divider(divider(...
    """

    def test_divides_two_integers_correctly(self):
        self.assertEqual(divider(10, 2), 5)

    def test_raises_an_exception_when_given_one_argument(self):
        self.assertRaises(TypeError, divider(10))

    def test_raises_an_exception_on_string_arguments(self):
        self.assertRaises(TypeError, divider(3,"12"))

    def test_raises_an_exception_on_dividing_by_zero(self):
        self.assertRaises(ValueError, divider(3, 0))

    def test_large_integer_dividends_and_divisors(self):
        # Test with large dividend and divisor
        large_dividend = 10**18
        large_divisor = 10**9
        result = divider(large_dividend, large_divisor)
        self.assertEqual(result, 10**9)

    def test_multiple_succession(self):
        self.assertEqual(divider(divider(10, 5), divider(4, 2), 1))

# Run the tests
if __name__ == '__main__':
    unittest.main()