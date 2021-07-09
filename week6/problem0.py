import os
import sys
import random


def sum_of_list(x):
    return sum(x)


def main():
    num_list = list(random.choices(range(1, 30), k=10))
    print(f"List of numbers: {num_list}")
    print(f"Sum of numbers: {sum_of_list(num_list)}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
