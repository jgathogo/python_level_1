import os
import sys
import random


def main():
    l1 = list(random.choices(range(100), k=100))
    l1 = list(random.choices(range(100), k=100))
    print(l1)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
