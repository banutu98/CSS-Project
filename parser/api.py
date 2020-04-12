from math import cos, sin
from .parser_math_functions import cartof

allowed_functions = [cos, sin, cartof]
allowed_operators = ['+', '-', '/', '*', '**', '(', ')']
allowed_variables = ['x']
