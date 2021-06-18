import os
import sys
import random
import string


def main():
    # Random sequence string of 100 base pairs
    alphabet = list(string.ascii_uppercase)
    residues = ['A', 'C', 'G', 'T']
    keys = random.choices(alphabet, k=50)
    values = random.choices(residues, k=50)
    pairs = list(zip(keys, values))
    sequence = ''
    for k in iter(pairs):
        sequence += k[0] + k[1]
    print(f"Random sequence of {len(sequence)} base pairs\n"
          f"{sequence}\n")

    # Print out k-mers
    k_list = [3, 4, 5, 6, 7]
    for k in iter(k_list):
        pos = 0
        d = {}
        print(f"k = {k}\n"
              f"{str(k) + '-mer'}\t\t\tcount\n"
              f"-------------------------")
        for i in iter(sequence):
            seq_temp = sequence[pos:]
            k_mer = seq_temp[0:k]
            if len(k_mer) == k:
                # print(k_mer)
                if k_mer not in d:
                    d[k_mer] = 1
                else:
                    d[k_mer] += + 1
            pos += 1
        for mer in iter(d):
            print(f"{mer}\t\t\t{d[mer]}")
        print("\n++++++++++++++++++++++++++\n")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
