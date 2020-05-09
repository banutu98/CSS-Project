from unittest import TestCase
from gui_components import parser
from math import tan


class ParserTestCase(TestCase):
    def test_ctan(self):
        self.assertEqual(parser.ctan(0.5), 1 / tan(0.5))

    def test__check_res(self):
        self.assertEqual(parser._check_res('2*x+3', 1), (True, 5))
        self.assertEqual(parser._check_res('2*x+vasiles(2)+3', 1), (False, 0))

    def test_get_integral_inside_expression(self):
        self.assertEqual(parser.get_integral_inside_expression('integrala(2+x)'), '2+x')
        self.assertEqual(parser.get_integral_inside_expression('5*x**2'), '')

    def test_check_expression_validity(self):
        self.assertEqual(parser.check_expression_validity(''), False)
        self.assertEqual(parser.check_expression_validity('integrala(2+x)'), True)
        self.assertEqual(parser.check_expression_validity('2+x'), True)
        self.assertEqual(parser.check_expression_validity('integrala('), False)
        self.assertEqual(parser.check_expression_validity('integrala22'), False)
        self.assertEqual(parser.check_expression_validity('integrala(22+5+x)'), True)

    def test_expr_to_lamda(self):
        currrent_lambda = lambda x: x * 2
        parser_lambda = parser.expr_to_lamda('x*2')
        self.assertEqual(currrent_lambda(2), parser_lambda(2))

    def test_check_expression_is_number(self):
        self.assertTrue(parser.check_expression_is_number('2.5'))
        self.assertFalse(parser.check_expression_is_number('vasile'))
