import os
import sys


def main():
    x = int(input("Enter value of x: "))

    try:
        num = (x ** 3) - (9 * x)
        den = (x ** 2) - (2 * x) + 1
        y = num / den
        print(f"y: {y}")

    except ZeroDivisionError as ze:
        print(f"Error when x = 1: {ze}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
