import os
import random
import sys

"""
Notes:
- Great job!

I've added an example below of a list comprehension. 

A list comprehension is a convenience that allows you to generate a list on-the-fly. 
It has the following syntax:

    l = <some list>
    output_list = [<operations on elements of l> for el in l]

For example, to double a list we could use:

    output_list = [2 * el for el in l]
    
The result does not have to be a list. It could be a generator, set or dictionary!

    output_generator = (2 * el for el in l) # notice we now use parentheses
    output_set = {2 * el for ele in l} # set comprehension
    output_dict = {el: 2 * el for el in l} # dict comprehension
    
My understanding is that comprehensions are blazing fast compared to for loops. 

You can also incorporate conditional in list comprehensions:

    output_list = [el for el in l if el % 2 == 0 else None]
"""


def main():
    # New list with cumulative sum
    l = list(random.choices(range(0, 100), k=100))
    print(l)

    print(f"Cumulative sum: ")
    new_l = []
    for i in range(len(l)):
        # very good!
        # there are many ways to accomplish this
        # I've added an extra one below
        new_l.append(sum(l[0:i + 1]))
    print(new_l)

    # start with the first value
    new_l2 = [l[0]]
    # iterate over beginning from the second value
    for i in l[1:]:
        # extend by adding the current from l with the last from new_l2
        new_l2 += [i + new_l2[-1]]
    print(new_l == new_l2)

    # New list of the sum of adjoining pairs
    print(f"Sum of adjoining pairs: ")
    new_l2 = []
    # fixme: instead of having the 'if' why not set the range to one less than l?
    # fixme: do you still need pos1 and pos2?
    for i in range(len(l) - 1):
        pos1 = i
        pos2 = pos1 + 1
        if pos1 < len(l) and pos2 < len(l):
            new_l2.append(l[pos1] + l[pos2])
    print(new_l2)
    # todo: you can add asserts to confirm whether everything is OK
    assert len(new_l2) + 1 == len(l)  # sanity check

    # List comprehension version
    new_l22 = [l[i] + l[i+1] for i in range(len(l) - 1)]
    assert new_l22 == new_l2

    # New list of the sum of 3 alternate values
    print(f"Sum of 3 alternate values")
    new_l3 = []
    i = 0  # redundant variable
    # fixme: same idea as above
    for i in range(len(l)):
        pos1 = i
        pos2 = pos1 + 2
        pos3 = pos2 + 2
        if pos1 < len(l) and pos2 < len(l) and pos3 < len(l):
            new_l3.append(l[pos1] + l[pos2] + l[pos3])
    print(new_l3)

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
