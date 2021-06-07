import os
import sys
import random


def main():
    number = input("Enter any number from 0 to 9: ")
    random_num = random.randint(0, 9)
    print(random_num)
    print(f"User number is: {number}, random number is: {random_num}. "
          f"\n Is user number less than random number? {int(number) < random_num}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
