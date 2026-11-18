import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 4), 0)
        self.assertEqual(add(2.5, 1.5), 4)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(3, 8), -5)
        self.assertEqual(subtract(5, 5), 0)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(5, 5), 25)

    def test_divide(self):
        self.assertEqual(div(2, 8), 4)
        self.assertEqual(div(3, 9), 3)
        self.assertEqual(div(5, 40), 8)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(5, -1)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(33, 56), 65)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(36), 6)


if __name__ == "__main__":
    unittest.main()
