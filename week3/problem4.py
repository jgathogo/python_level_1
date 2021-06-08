import os
import sys
import random


def main():
    random_list = list(random.choices(range(5), k=10))

    print(f"Number of times each number is present in list: \n"
          f"0: {random_list.count(0)}\n"
          f"1: {random_list.count(1)}\n"
          f"2: {random_list.count(2)}\n"
          f"3: {random_list.count(3)}\n"
          f"4: {random_list.count(4)}\n"
          f"5: {random_list.count(5)}\n")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
