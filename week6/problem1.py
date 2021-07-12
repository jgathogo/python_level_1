import os
import random
import sys

"""
Notes:
- OK but please flesh these out without relying on the inbuilt functions. I've updated the challenge text to reflect this
- Please add a docstring to your function in line with the notes provided.
"""


def max_min(x):
    # fixme: do not use builtins
    return max(x), min(x)


def main():
    num_list = list(random.choices(range(1, 30), k=10))
    print(f"List of numbers: {num_list}")
    print(f"Max: {max_min(num_list)[0]} Min: {max_min(num_list)[1]}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
