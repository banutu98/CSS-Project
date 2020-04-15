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
        return eval(expression), True
    except Exception as e:
        print(e)
        return 0, False


def check_expression_validity(expression: str, x: float) -> (bool, int):
    split_expr = checking_regex.split(expression)
    for token in split_expr:
        if token is not None and token is not '':  # not null
            if token not in allowed_variables and token not in function_names:  # not recognized
                if not token.isnumeric():  # not a number
                    print(token)
                    return False, 0

    return _check_res(expression, x)


if __name__ == '__main__':
    for expr in expressions:
        ok = check_expression_validity(expr, 2)
        print(expr + ' -> ' + str(ok))
        if ok:
            print('value: {}'.format(check_expression_validity(expr, 0)))
