import re
from math import cos, sin


# from .api import *

# from math import cos, sin
# from .parser_math_functions import cartof

def cartof(x):
    return x * 5


allowed_functions = [cos, sin, cartof]
allowed_operators = ['+', '-', '/', '*', '**', '(', ')']
allowed_variables = ['x']

# allowed_functions = [cos, sin, cartof]
# allowed_operators = ['+', '-', '/', '*', '**', '(', ')']
# allowed_variables = ['x']

function_names = [func.__name__ for func in allowed_functions]

all_allowed_things = function_names[:]
all_allowed_things.extend(allowed_operators)
all_allowed_things.extend(allowed_variables)

checking_regex = re.compile('|'.join([re.escape(token) for token in allowed_operators]))

expressions = ['vasile(2+x)+5', 'x+1+2+3/5*6', 'sin(0*2)+3', 'cos(x)*5', 'cartof(2)+2',
               'xxx+2', '-1', 'sin+2', '3cartof', '3x', 'x*2', 'x**2']


def _check_res(expression, x):
    try:
        return True, eval(expression)
    except Exception as e:
        print(e)
        return False, 0


def get_integral_inside_expression(expression: str) -> str:
    if expression.startswith('integral'):
        expression = expression.lstrip('integral')
        if len(expression) < 2:
            return ''
        if expression[0] != '(' or expression[len(expression) - 1] != ')':
            return ''
        expression = expression[1:]
        expression = expression[:len(expression) - 1]
        return expression
    return ''


def check_expression_validity(expression: str) -> bool:
    expression = expression.replace(' ', '')  # ignore spaces
    if len(expression) == 0:
        return False
    integral_expr = get_integral_inside_expression(expression)
    if integral_expr != '':
        expression = integral_expr
    if expression.startswith('integral'):
        expression = expression.lstrip('integral')
        if len(expression) < 2:
            return False
        if expression[0] != '(' or expression[len(expression) - 1] != ')':
            return False
        expression = expression[1:]
        expression = expression[:len(expression) - 1]

    split_expr = checking_regex.split(expression)
    for token in split_expr:
        if token is not None and token is not '':  # not null
            if token not in allowed_variables and token not in function_names:  # not recognized
                if not check_expression_is_number(token):
                    return False
    return True


def expr_to_lamda(expression: str):
    return eval('lambda x: {}'.format(expression))


def check_expression_is_number(expression: str):
    try:
        float(expression)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    for expr in expressions:
        ok = check_expression_validity(expr)
        print(expr + ' -> ' + str(ok))
        if ok:
            print('value: {}'.format(check_expression_validity(expr)))
