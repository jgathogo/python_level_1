import os
import sys
import random


def main():
    # New list with cumulative sum
    l = list(random.choices(range(0, 100), k=100))
    print(l)

    print(f"Cumulative sum: ")
    new_l = []
    i = 0
    while i < len(l):
        new_l.append(sum(l[0:i + 1]))
        i += 1
    print(new_l)

    # New list of the sum of adjoining pairs
    print(f"Sum of adjoining pairs: ")
    new_l2 = []
    i = 0
    while i < len(l) - 1:
        pos1 = i
        pos2 = pos1 + 1
        new_l2.append(l[pos1] + l[pos2])
        i += 1
    print(new_l2)

    # New list of the sum of 3 alternate values
    print(f"Sum of 3 alternate values")
    new_l3 = []
    i = 0
    while i < len(l) - 1:
        pos1 = i
        pos2 = pos1 + 2
        pos3 = pos2 + 2
        if pos1 < len(l) and pos2 < len(l) and pos3 < len(l):
            new_l3.append(l[pos1] + l[pos2] + l[pos3])
        i += 1
    print(new_l3)

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
