import unittest
from string_calculator.string_calculator import string_calculator

# Unit tests for the string_calculator function
class TestStringCalculator(unittest.TestCase):

    # Test: should return 0 for an empty string input
    def test_empty_string(self):
        result = string_calculator("")
        self.assertEqual(result, 0)
    
    # Test: should return the number itself when a single number is passed
    def test_single_number(self):
        result = string_calculator("1")
        self.assertEqual(result, 1)
        
    # Test: should return the sum of two numbers separated by a comma
    def test_two_numbers(self):
        result = string_calculator("1,2")
        self.assertEqual(result, 3)
        
    # Test: should return the sum of multiple numbers separated by commas
    def test_multiple_numbers(self):
        result = string_calculator("1,2,3")
        self.assertEqual(result, 6)
        
    # Test: should handle newlines as delimiters along with commas
    def test_newline_delimiter(self):
        result = string_calculator("1\n2,3")
        self.assertEqual(result, 6)
        
    # Test: should support custom delimiters specified in the input
    def test_custom_delimiter(self):
        result = string_calculator("//;\n1;2")
        self.assertEqual(result, 3)

    # Test: should raise a ValueError when negative numbers are passed
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            string_calculator("1,-2,3")
            print(" context.exception ", context.exception)
        self.assertTrue("Negative numbers not allowed" in str(context.exception))