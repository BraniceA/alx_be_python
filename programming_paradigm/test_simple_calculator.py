import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method"""
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(10, -5), 5)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(5, -5), 0)
        self.assertEqual(self.calc.add(5, 0), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(5, -5), 10)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(10, -5), -50)
        self.assertEqual(self.calc.multiply(-10, 5), -50)
        self.assertEqual(self.calc.multiply(5, -5), -25)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        self.assertEqual(self.calc.multiply(-5, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(10, -5), -2)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(5, -5), -1)
        self.assertEqual(self.calc.divide(5, 0), None)

if __name__== '__main__':
    unittest.main()
