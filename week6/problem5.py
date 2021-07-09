import os
import sys


def repeat_characters(word, num=2):
    rep = ""
    for char in word:
        rep += char * num
    return rep


def main():
    w = "abcdefg"
    print(repeat_characters(w, num=4))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
