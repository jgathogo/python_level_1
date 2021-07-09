import os
import sys
import random


def max_min(x):
    return max(x), min(x)


def main():
    num_list = list(random.choices(range(1, 30), k=10))
    print(f"List of numbers: {num_list}")
    print(f"Max: {max_min(num_list)[0]} Min: {max_min(num_list)[1]}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
