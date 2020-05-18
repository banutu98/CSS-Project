from math import log
from gui_components.defines import *
from math import sin, cos, tan, asin, acos, atan, sqrt


def ctan(x):
    return 1 / tan(x)


def integral(func, lower_bound, upper_bound, nr_rectangles=10000):
    assert callable(func)
    assert isinstance(lower_bound, float)
    assert isinstance(upper_bound, float)
    assert upper_bound > lower_bound
    assert nr_rectangles == NR_RECTANGLES

    integral_result = 0
    rectangle_width = (upper_bound - lower_bound) / nr_rectangles

    assert rectangle_width > 0
    for i in range(nr_rectangles):
        x = lower_bound + i * rectangle_width
        integral_result += rectangle_width * func(x)

    return integral_result


if __name__ == "__main__":
    print("Math functions library for Plot Master")
