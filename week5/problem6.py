import os
import sys

"""
Notes:
- Excellent!
- See notes below.
"""


def main():
    user_input = input("Enter a sentence: ").split(" ")
    sentence = dict(enumerate(user_input))  # really clever
    for index, word in sentence.items():
        print(f"{index} --> {word}")

    # you can also use enumerate directly in a for loop
    # this will save memory if the original list is large
    user_input = input("Enter another sentence: ").split()  # ' ' is the default split char
    for index, word in enumerate(user_input):
        print(f"{index} --> {word}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
