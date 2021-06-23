import os
import sys
import random
import string


def main():
    # Create 2 dictionaries each with random assortment of letters
    values_d1 = random.choices(range(100), k=10)
    keys_d1 = random.choices(string.ascii_lowercase, k=10)
    d1 = dict(zip(keys_d1, values_d1))

    values_d2 = random.choices(range(100), k=10)
    keys_d2 = random.choices(string.ascii_lowercase, k=10)
    d2 = dict(zip(keys_d2, values_d2))
    print(d1)
    print(d2)

    dsum = {}
    for w in iter(d1):
        if w in d2:
            if w in dsum:
                dsum[w] += d1[w] + d2[w]

            else:
                dsum[w] = d1[w] + d2[w]
        else:
            dsum[w] = d1[w]

    for w in iter(d2):
        if w in d1:
            if w in dsum:
                dsum[w] += d1[w] + d2[w]

            else:
                dsum[w] = d1[w] + d2[w]
        else:
            dsum[w] = d2[w]

    print(dsum)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
