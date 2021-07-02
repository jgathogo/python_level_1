import os
import random
import sys

"""
Notes:
- Excellent!
- I would invite you to consider going through these problems again to improve your code
based on what you have learned from the harder problems. 
"""


def main():
    l1 = list(random.choices(range(100), k=100))
    l2 = list(random.choices(range(100), k=100))

    # l1 = [2, 2, 3, 4, 5]
    # l2 = [3, 4, 5, 6, 7]
    print(f"l1: {l1}\n"
          f"l2: {l2}")

    l3 = []
    for i in range(len(l1)):
        # great!
        l3.append(l1[i] + l2[i])
    print(f"Pairwise sums: {l3}")

    cum_prod = []
    for i in range(len(l1)):
        cum_prod.append(sum(cum_prod) + l1[i] * l2[i])
    print(f"Cumulative pairwise products: {cum_prod}")

    even_odd = []
    for i in range(len(l1)):
        if (l1[i] % 2 == 0 and l2[i] % 2 == 0) or (l1[i] % 2 != 0 and l2[i] % 2 != 0):
            even_odd.append(l1[i] + l2[i])

    print(f"Sums of even/odd pairs: {even_odd}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
