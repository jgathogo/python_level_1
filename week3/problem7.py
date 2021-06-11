import os
import sys

"""
Notes:
- parentheses are not needed for ** and * operators
"""


def main():
    x = int(input("Enter value of x: "))

    try:
        # fixme: should be
        #  num = x ** 3 - 9 * x
        num = (x ** 3) - (9 * x)
        # fixme: should be
        #  den = x ** 2 - 2 * x + 1
        den = (x ** 2) - (2 * x) + 1
        y = num / den
        print(f"y: {y}")

    except ZeroDivisionError as ze:
        print(f"Error when x = 1: {ze}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
