import os
import sys
import random


def main():
    random_list = list(random.choices(range(50, 75), k=100))
    min_l = min(random_list)
    max_l = max(random_list)

    l_sorted = sorted(random_list)

    first_letter = l_sorted[0]
    last_letter = l_sorted[-1]
    print(l_sorted)
    print(f"min = {min_l}")
    print(f"max = {max_l}")

    print(f"Minimum and the first number are equal: {min_l == first_letter}\n"
          f"Maximum and the last number are equal: {max_l == last_letter}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
