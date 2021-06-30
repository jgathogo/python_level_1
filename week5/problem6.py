import os
import sys


def main():
    user_input = input("Enter a sentence: ").split(" ")
    sentence = dict(enumerate(user_input))
    for index, word in sentence.items():
        print(f"{index} --> {word}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
