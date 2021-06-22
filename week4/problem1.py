import os
import sys
import random
import string

"""
Notes:
- You can replace 'alphabet' with residues (or a string with the 
same characters in 'residues' to get a 'true' DNA sequence
"""

def main():
    # Random sequence string of 100 base pairs
    alphabet = list(string.ascii_uppercase) # redundant
    residues = ['A', 'C', 'G', 'T']
    # I've replaced alphabet with residues
    keys = random.choices(residues, k=50)
    # fixme: 'values' is redundant; it is not?
    values = random.choices(residues, k=50)
    # fixme: no need for zip()
    pairs = list(zip(keys, values))
    sequence = ''
    # fixme: no need for iter()
    for k in iter(pairs):
        sequence += k[0] + k[1]
    print(f"Random sequence of {len(sequence)} base pairs\n"
          f"{sequence}\n")

    # Print out k-mers
    k_list = [3, 4, 5, 6, 7]
    # fixme: no need for iter()
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
            # fixme: i is not being used; can you replace pos
            #  with i since the for loop gives you i for free?
            pos += 1
        for mer in iter(d):
            print(f"{mer}\t\t\t{d[mer]}")
        print("\n++++++++++++++++++++++++++\n")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
