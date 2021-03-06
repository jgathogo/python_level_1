import os
import random
import sys

"""
Notes:
- While this does the job it just defers the operation of summing
- Let me add a bit more complexity: include a parameter which specifies at what value the sum should begin:
    sum_of_list(some_list, start_at=10)
    sum_of_list(list(range(1, 10)), start_at=20) should give 75
- Please add a docstring to your function in line with the notes provided.
"""


def sum_of_list(num_list, start_at=10):
    """Sum the numbers in a list

    >>> sum_of_list(list(range(1, 10), start_at=2)

    """
    # fixme: please have another go at this; write your own sum implementation 😉
    sum_num = 0
    end_at = len(num_list)
    for i in range(start_at, end_at):
        sum_num += num_list[i]
    return sum_num


def main():
    # num_list = list(random.choices(range(1, 30), k=10))
    num_list = [1, 2, 3, 4, 5]

    print(f"List of numbers: {num_list}")
    print(f"Sum of numbers: {sum_of_list(num_list)}")
    print(sum_of_list(list(range(1, 100)), start_at=20))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
