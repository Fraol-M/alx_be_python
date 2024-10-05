import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):


    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(55.23, -2.5), 52.73)
        self.assertEqual(self.calc.add(5523, -2.0045), 5520.9955)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(55.23, -2.5), 57.73)
        self.assertEqual(self.calc.subtract(5523, -2.0045), 5525.0045)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(55.23, -2.5), -138.075)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(55.23, -2.5), -22.092)
        self.assertAlmostEqual(self.calc.divide(2, 3), 2/3)
        self.assertIsNone(self.calc.divide(5,0))
        self.assertEqual(self.calc.divide(0, 3), 0)

if __name__ == '__main__':
    unittest.main()