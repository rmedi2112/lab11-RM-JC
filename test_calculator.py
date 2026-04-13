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
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(4, 9), 36)
        self.assertEqual(mul(-3, 5), -15)
        self.assertEqual(mul(0, 2), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 27), 9)
        self.assertEqual(div(1, 5), 5)
        self.assertEqual(div(-2, 10), -5)
    # ##########################

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
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(1, 6)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypothenuse(3, 4), 5)
        self.assertEqual(hypothenuse(5, 12), 13)
        self.assertEqual(hypothenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-2)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(100), 10)
        
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()