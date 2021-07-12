import os
import sys

"""
Notes:
- Great job! ask the user for input 😄
- Please add a docstring to your function in line with the notes provided.
"""


def is_palindrome(text):
    return text == text[::-1]


def main():
    s = "step on no pets"
    if is_palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
