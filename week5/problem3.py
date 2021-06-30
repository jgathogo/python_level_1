import os
import sys
import random


def main():
    l1 = list(random.choices(range(100), k=100))
    l2 = list(random.choices(range(100), k=100))
    print(f"l1: {l1}\n"
          f"l2: {l2}")

    l3 = []
    i = 0
    while i < len(l2):
        # for i in range(len(l1)):
        l3.append(l1[i] + l2[i])
        i += 1
    print(f"Pairwise sums: {l3}")

    cum_prod = []
    i = 0
    while i < len(l2):
        # for i in range(len(l1)):
        cum_prod.append(sum(cum_prod) + l1[i] * l2[i])
        i += 1
    print(f"Cumulative pairwise products: {cum_prod}")

    even_odd = []
    i = 0
    while i < len(l1):
        # for i in range(len(l1)):
        if (l1[i] % 2 == 0 and l2[i] % 2 == 0) or (l1[i] % 2 != 0 and l2[i] % 2 != 0):
            even_odd.append(l1[i] + l2[i])
        i += 1

    print(f"Sums of even/odd pairs: {even_odd}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
