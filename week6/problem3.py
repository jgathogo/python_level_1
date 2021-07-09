import os
import sys


def reverse_string(s):
    rev_str = ''
    pos = len(s) - 1
    while pos >= 0:
        rev_str += s[pos]
        pos -= 1
    return rev_str


def main():
    s = "step on no pets"
    print(reverse_string(s))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
