# Author: @simonaprs
# ----------------------------------------------------------------------------
# Imports
import unittest
from main import *


class MyTestCase(unittest.TestCase):

    def test_input_correct(self):
        """ Tests for values that should produce correct value of input """
        expression = '5 2 /'
        input_valid = check_input(expression)
        self.assertEqual(input_valid, True)

    def test_input_incorrect(self):
        """ Tests for values that should produce incorrect value of input """
        expression = '5 s d 6/'
        input_valid = check_input(expression)
        self.assertEqual(input_valid, False)

    # Test for values that should produce correct value of result
    def test_result(self):
        """ Test for values that should produce correct value of result """
        expression = '2 3 * 11 14 * +'
        result = calculate(expression)
        self.assertEqual(result, 160)

if __name__ == '__main__':
    unittest.main()
