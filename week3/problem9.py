import os
import sys


def main():
    x = int(input("Type greater number(x): "))
    y = int(input("Type smaller number(y): "))
    assert x > y, "x must be greater than y"

    z = list(range(x, y - 1, -1))
    print(f"Values in descending order, from {x} to {y}:\n"
          f"{z}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
