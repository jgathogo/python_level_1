import os
import sys


def main():
    int_start = int(input("Enter the start digit: "))
    int_stop = int(input("Enter the stop number: "))
    int_step = int(input("Enter the step number: "))

    print(f"Generated integers: {list(range(int_start, int_stop, int_step))}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
