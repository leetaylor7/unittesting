# this is the parent module, good for basic logging
import unittest

# this allows you to test classes
from unittest import TestCase


### Example
class TestSubroutine(TestCase):
    """Verifies subroutine beharvior"""

    # standard methond naming is test_
    def test_subroutine_with_no_arguments(self):
        pass

### Example Add Function
def adder(x, y):
    return x + y

class TestAdder(TestCase):
    def test_adds_three_and_five_correctly(self):
        self.assertEqual(adder(3, 5), 8, "Adding 3 and 5 should produce 8") # This provides more detail about the test

    def test_adds_integer_and_string_raises_exception(self):
        try:
            result = adder(3, "12")
        except Exception as e:
            self.assertIsInstance(e, TypeError)
        else:
            self.fail('Did not raise Exception')

        # Alternatively
        # self.assertRaises(TypeError, adder, 3, "12")