import os
import sys
import random


def main():
    random_list = list(random.choices(range(10), k=5))
    number_entered = int(input("Enter any number between 0 and 9: "))

    print(f"Numbers generated are: {random_list}\n"
          f"Check if computer excluded {number_entered} : {number_entered not in random_list}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
