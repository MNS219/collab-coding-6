import unittest
from main import addn   # make sure your function in main.py is named addn

class TestAddNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(addn(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(addn(-2, -3), -5)

    def test_mixed_numbers(self):
        self.assertEqual(addn(-2, 5), 3)

    def test_zero(self):
        self.assertEqual(addn(0, 7), 7)
        self.assertEqual(addn(0, 0), 0)

if __name__ == "__main__":
    unittest.main()

