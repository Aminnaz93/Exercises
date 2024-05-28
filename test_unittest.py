from functions import *
import unittest


class TestCalcFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        result = add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=15, msg="Should be approximately 0.3")

    def test_sub(self):
        self.assertEqual(sub(3, 1), 2)
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(5, 10), -5)

    def test_mult(self):
        self.assertEqual(mult(2, 3), 6)
        self.assertEqual(mult(0, 5), 0)
        self.assertEqual(mult(-4, 2), -8)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(-10, 5), -2)

        # Test för att undvika division med noll
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

if __name__ == '__main__':
    unittest.main()
