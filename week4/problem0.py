import os
import sys


def main():
    text = input("Enter a ten character word: ")

    if len(text) != 10:
        print("Number of characters should be exactly 10 in number.\n"
              "Please run the program again and enter exactly 10 characters")

    d = {}

    for i in text:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
