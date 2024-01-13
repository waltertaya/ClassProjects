import unittest
from arithmetic import Arithmetic


class TestArithmetic(unittest.TestCase):
    """
    This is a class for arithmetic operations like addition and multiplication
    """

    def setUp(self):
        self.arithmetic_1 = Arithmetic(10, 5)
        self.arithmetic_2 = Arithmetic(23, 10)
        self.arithmetic_3 = Arithmetic(-50, 8)
        self.arithmetic_4 = Arithmetic(9, 0)
        self.arithmetic_5 = Arithmetic(0, 0)

    def test_add(self):
        self.assertEqual(self.arithmetic_1.add(), 15)
        self.assertEqual(self.arithmetic_2.add(), 33)
        self.assertEqual(self.arithmetic_3.add(), -42)
        self.assertEqual(self.arithmetic_4.add(), 9)
        self.assertEqual(self.arithmetic_5.add(), 0)

    def test_mul(self):
        self.assertEqual(self.arithmetic_1.mul(), 50)
        self.assertEqual(self.arithmetic_2.mul(), 230)
        self.assertEqual(self.arithmetic_3.mul(), -400)
        self.assertEqual(self.arithmetic_4.mul(), 0)
        self.assertEqual(self.arithmetic_5.mul(), 0)

    def test_div(self):
        self.assertEqual(self.arithmetic_1.div(), 2)
        self.assertEqual(self.arithmetic_2.div(), 2.3)
        self.assertEqual(self.arithmetic_3.div(), -6.25)
        # with self.assertRaises(self.arithmetic_4.div()):
        #     ZeroDivisionError
        # with self.assertRaises(self.arithmetic_5.div()):
        #     ZeroDivisionError

    def test_sub(self):
        self.assertEqual(self.arithmetic_1.sub(), 5)
        self.assertEqual(self.arithmetic_2.sub(), 13)
        self.assertEqual(self.arithmetic_3.sub(), -58)
        self.assertEqual(self.arithmetic_4.sub(), 9)
        self.assertEqual(self.arithmetic_5.sub(), 0)
