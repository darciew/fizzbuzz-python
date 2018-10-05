import unittest
from fizzbuzz import *

class FizzBuzzTest(unittest.TestCase):

    def test_print_fizzbuzz_if_divisible_by_fifteen(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")

    def test_prints_fizz_if_divisible_by_three(self):
        self.assertEqual(FizzBuzz(3), "Fizz")

    def test_prints_buzz_if_divisible_by_five(self):
        self.assertEqual(FizzBuzz(5), "Buzz")

    def test_prints_number_if_not_divisible(self):
        self.assertEqual(FizzBuzz(2), 2)

if __name__ == '__main__':
    unittest.main()
