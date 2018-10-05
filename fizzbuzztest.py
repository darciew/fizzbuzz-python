import unittest
from fizzbuzz import *

class FizzBuzzTest(unittest.TestCase):

    def test_print_fizzbuzz_if_divisible_by_fifteen(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
