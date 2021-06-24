import os
import random
import string
import sys

"""
Notes:
- In my experience, I sense you are currently at an important juncture in your
learning: you are reaching the limits of your mental memory. This is evident 
because your code is hard to follow meaning that you are trying to juggle
everything in your head, and that is very hard. In fact, it is also
very stressful and can interfere with your joy of learning. I propose following
two steps below (write these down and try them out for every problem):

1. substitute the original problem with a far, far simpler one
instead of making a big dictionary start with the most most basic
d1 = {'a': 1} and d2 = {'a': 1}

2. solve the problem in (1) *on paper* first; do not write any code until
you have a good grasp of the moving parts; the key question you should 
ask is "how do I gradually transform the inputs into the desired outputs?";
then make it slightly more difficult then repeat until you have 
something like the real one e.g. 
d1 = {'a': 1, 'b': 2} and d2 = {'b': 5, 'z': 10}

This is the skill of abstraction, the ability to simplify an actual 
problem into the essential steps required to solve it. 
It is at the heart of programming. For some people it comes far 
easier than for others but I think of it like learning to ride a bicycle: 
no one can tell you exactly how but once you know how you just know.
"""


def main():
    # Create 2 dictionaries each with random assortment of letters
    values_d1 = random.choices(range(100), k=2)
    keys_d1 = random.choices(string.ascii_lowercase, k=2)
    d1 = dict(zip(keys_d1, values_d1))

    values_d2 = random.choices(range(100), k=10)
    keys_d2 = random.choices(string.ascii_lowercase, k=10)
    d2 = dict(zip(keys_d2, values_d2))

    dsum = {}

    for k, v in d1.items():
        if k in d2:
            dsum[k] = d1[k] + d2[k]
        else:
            dsum[k] = v

    for k, v in d2.items():
        if k not in dsum:
            dsum[k] = v

    print(dsum)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
