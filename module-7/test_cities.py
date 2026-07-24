# Import the unittest for writing and running tests
import unittest
# Import the function to test from city_functions.py file
from city_functions import city_country


# Create a test case class that inherits from unittest.TestCase
class CitiesTestCase(unittest.TestCase):

    # Define a test method
    def test_city_country(self):

        # Call the imported function with basic test data and store the result
        formatted_string = city_country('santiago', 'chile')

        # Check that the function's output matches exactly what is expected
        self.assertEqual(formatted_string, 'Santiago, Chile')


# Ensures the testing framework runs automatically when this file is executed
if __name__ == '__main__':
    unittest.main()