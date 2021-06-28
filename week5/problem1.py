import os
import sys
import random


def main():
    # l1 = list(random.choices(range(100), k=100))
    # l2 = list(random.choices(range(100), k=100))

    l1 = [1, 2, 3, 4, 5]
    l2 = [3, 4, 5, 6, 7]
    print(f"l1: {l1}\n"
          f"l2: {l2}")

    l3 = []
    i = 0
    for num in l1:
        l3.append(l1[i] + l2[i])
        i += 1
    print(l3)

    l4_even = []
    l4_odd = []
    i = 0
    for num in l1:
        if l1[i] % 2 == 0 and l2[i] % 2 == 0:
            l4_even.append(l1[i] + l2[i])
        elif l1[i] % 2 != 0 and l2[i] % 2 != 0:
            l4_odd.append(l1[i] + l2[i])
        i += 1
    print(f"l4_even {l4_even}\n"
          f"l4_odd {l4_odd}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
