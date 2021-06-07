import os
import sys

"""
Notes:
- see comment in problem0.py on first line of docstring
- see comment in problem1.py on return value; if the return value is None then we leave out the 'return' from the docstring
- Your program has no exit code!
"""


def print_name_age_77():
    """ Ask user their name and age. Print out their year of birth and year when they will be 77 years"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))  # this is the key; casting to an int

    # good variable names; something like 'yob' would also do
    year_of_birth = 2021 - age
    year_77 = 2021 + (77 - age)

    print(f"Your name is {name} and you are {age} years old. Your were born in {year_of_birth}. You will be 77 years "
          f"in {year_77}")


def main():
    print_name_age_77()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
