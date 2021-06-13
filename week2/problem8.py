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

A complex number is made up of two parts: real and imaginary. Python allows us 
to represent complex numbers by passing the real and imaginary parts as arguments 
to the complex() class. For example,

complex(1, 2) 

returns the complex number (1+2j): 1 is real and 2j is imaginary.

Now, when we are trying to solve (I will only handle the case with +; the one with - is the same) 

x = (-b + math.sqrt(b**2 - 4*a*c)/(2*a)

or
    -b + math.sqrt(b**2 - 4*a*c)
x = ----------------------------.
              2*a
              
We can write this as 

    ⎡   b ⎤ ⎡math.sqrt(b**2 - 4*a*c)⎤
x = ⎢- ---⎢+⎢-----------------------⎢
    ⎣  2*a⎦ ⎣      2*a              ⎦
    
Now the right has two values: the one first one is always real but the second one 
becomes imaginary when the discriminant is negative. Please see the slide titled
Complex Math in week3 slides.

This will give you enough to work on to solve the problem. I'd like you to experience
the joy of solving it for yourself.
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
