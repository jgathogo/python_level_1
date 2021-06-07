import sys
import os
import math

"""
Notes:
- Excellent docstrings
"""


def calculate(a, b, c):
    """ Solve quadratic equation and return the value of x

    :param float a: coefficient of x^2
    :param float b: coefficient of x
    :param float c: constant
    :return: both solutions
    :rtype: tuple(float, float)
    """
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return None, None
    x1 = (2 * c) / (-b + math.sqrt(discriminant))
    x2 = (2 * c) / (-b - math.sqrt(discriminant))
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1}, x2={x2}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
