from calculator1.source1.calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_power(self):
        calc = Calculator()
        result = calc.power(2, 3)
        self.assertEqual(result, 8)
        result = calc.power(3, 3)
        self.assertEqual(result, 27)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(8, 2)
        self.assertEqual(result, 4)
        result = calc.divide(33, 3)
        self.assertEqual(result, 11)
