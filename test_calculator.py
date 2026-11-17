import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(5, 5), 25)

    def test_divide(self):
        self.assertEqual(div(2,8),4)
        self.assertEqual(div(3, 9), 3)
        self.assertEqual(div(5, 40), 8)


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(5,-1)
        with self.assertRaises(ValueError):
            logarithm(-3,50)


    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(33, 56), 65)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(0)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(36), 6)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
