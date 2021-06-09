import os
import sys


def main():
    # no need for int_* in the variable name
    start = int(input("Enter the start digit: "))
    stop = int(input("Enter the stop number: "))
    step = int(input("Enter the step number: "))

    print(f"Generated integers: {list(range(start, stop, step))}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
