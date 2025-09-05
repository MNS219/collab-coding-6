import unittest

from main import div   # replace 'your_module' with the actual filename (without .py)

class TestDivision(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(9, 2), 4)   # floor division

    def test_negative_numbers(self):
        self.assertEqual(div(-10, 2), -5)
        self.assertEqual(div(10, -3), -4) # floor division rounds down

    def test_zero_dividend(self):
        self.assertEqual(div(0, 5), 0)

    def test_divide_by_one(self):
        self.assertEqual(div(7, 1), 7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

if __name__ == "__main__":
    unittest.main()
