#https://github.com/mfarmer5/lab11-MF-AR
#Partner 1: Mahak Farmer
#Partner 2: Aashita Rai

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2

    # ##########################

    ######## Partner 1
    def test_multiply(self, a, b): # 3 assertions
       assert (mul(5, 6))
       assert (mul(7, 4))
       assert (mul(8, 3))
    def test_divide(self): # 3 assertions
        assert (div(4, 2))
        assert(div(0, 6))
        assert(div(1, 1))

    # ##########################

    ######## Partner 2

    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):# 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(10, 5)
        assert hypotenuse(16, 4)
        assert hypotenuse(3, 3)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(0), 0)

        self.assertEqual(square_root(25), 5)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()