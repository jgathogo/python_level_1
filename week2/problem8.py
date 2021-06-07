import sys
import os
import math


"""
Notes
- The trick here is to split the right hand side (RHS) of the equation into two 
fractions i.e. x = -b/2/a +/- math.sqrt(discriminant)/2/a
- The discriminant is >= 0 for real roots and < 0 for imaginary roots
- For real roots: x1,2 = -b/2/a +/- math.sqrt(discriminant)/2/a as usual
- For complex roots: 
    x1 = complex(-b/2/a, math.sqrt(-discriminant)/2/a)
    x2 = complex(-b/2/a, -math.sqrt(-discriminant)/2/a)
I've leave it to your to experience the joy of solving it
"""


def calculate(a, b, c):
    """ Solve quadratic equation and return the value of x

    :param float a: coefficient of x^2
    :param float b: coefficient of x
    :param float c: constant
    :return: both solutions
    :rtype: tuple(float, float)
    """
    discriminant = b ** 2 - 4 * a * c
    disc_complex = complex(discriminant, math.sqrt(-discriminant)/(2 * a))

    print(f"Discriminant: {discriminant} Complex: {disc_complex}")
    if discriminant < 0:
        return None, None
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
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
