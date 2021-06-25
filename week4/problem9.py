import os
import sys


def main():
    stop = 1000
    one = set(range(2, stop))
    two = set(range(4, stop, 2))
    three = set(range(6, stop, 3))
    five = set(range(10, stop, 5))
    seven = set(range(14, stop, 7))

    x = one - two - three - five - seven
    print(sorted(x))

    # The values in the resulting set are prime numbers
    # To provide values to 1000, change stop value in range

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
