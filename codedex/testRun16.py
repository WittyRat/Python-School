"""Let’s test a simple add_numbers() function that takes two numbers as input and returns their sum.

First, open your local editor and create a new test_addition.py file. Then, copy/paste the code below:"""

import unittest

def add(a, b):
  return a + b

class TestAddition(unittest.TestCase):
  # Define the first unit test
  def test_add(self):
    result = add(3, 4)

    # Define the expected result
    expected_result = 9
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()