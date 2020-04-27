from math import log
from math import sin, cos


def integral(fnc_expression, lower_bound, upper_bound, nr_rectangles=10000):
    integral_result = 0
    rectangle_width = (upper_bound - lower_bound) / nr_rectangles

    for i in range(nr_rectangles):
        x = lower_bound + i * rectangle_width
        integral_result += rectangle_width * eval(fnc_expression)

    return integral_result


if __name__ == "__main__":
    print("Math functions library for Plot Master")
