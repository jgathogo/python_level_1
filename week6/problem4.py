import os
import random
import sys

"""
Note:
- Good try but this does not double!
"""


def main():
    f_l = []
    for num in range(15):
        f_l.append(round(random.uniform(1, 10), 2))
    print(f"List of floats: {f_l}")
    double = list(map(lambda x: round(x ** 2, 2), f_l))
    print(f"Doubles: {double}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
