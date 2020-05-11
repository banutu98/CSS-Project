import unittest
from math_functions.math_functions import integral
from gui_components import parser


class TestMathFunctions(unittest.TestCase):

    def test_inverse_function_integral(self):
        function = parser.expr_to_lamda("1/x")
        positive_interval_result = 2.30258
        negative_interval_result = -2.30258

        self.assertAlmostEqual(integral(function, 1, 10), positive_interval_result, places=1)
        self.assertAlmostEqual(integral(function, -10, -1),
                               negative_interval_result, places=1)
        self.assertRaises(ZeroDivisionError, integral, function, 0, 1)

    def test_second_degree_function_integral(self):
        function = parser.expr_to_lamda("x**2 + 1")
        positive_interval_result = 342
        negative_interval_value = 342

        self.assertAlmostEqual(integral(function, 1, 10), positive_interval_result, places=1)
        self.assertAlmostEqual(integral(function, -10, -1), negative_interval_value, places=1)

    def test_sin_function_integral(self):
        function = parser.expr_to_lamda("sin(x)")
        positive_interval_value = 1.37937
        negative_interval_value = -1.37937

        self.assertAlmostEqual(integral(function, 1, 10), positive_interval_value, places=1)
        self.assertAlmostEqual(integral(function, -10, -1), negative_interval_value, places=1)

    def test_cos_function_integral(self):
        function = parser.expr_to_lamda("cos(x)")
        positive_interval_value = -1.38549
        negative_interval_value = -1.38549

        self.assertAlmostEqual(integral(function, 1, 10), positive_interval_value, places=1)
        self.assertAlmostEqual(integral(function, -10, -1), negative_interval_value, places=1)

    def test_sqrt_function_integral(self):
        function = parser.expr_to_lamda("sqrt(x)")
        positive_interval_value = 20.41518

        self.assertAlmostEqual(integral(function, 1, 10), positive_interval_value, places=1)
        self.assertRaises(ValueError, integral, function, -1, -10)

    def test_tangent_function_integral(self):
        function = parser.expr_to_lamda("tan(x)")
        positive_interval_value = 0.61562
        negative_interval_value = -0.61562

        self.assertAlmostEqual(integral(function, 0, 1), positive_interval_value, places=1)
        self.assertAlmostEqual(integral(function, -1, 0), negative_interval_value, places=1)

        ###THIS SHOULD FAIL###
        self.assertEqual(integral(function, 1, 10), "undefined")


if __name__ == "__main__":
    unittest.main()
