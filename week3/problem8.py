import os
import sys


def main():
    # no need for int_* in the variable name
    # the variables had been int_start, which wasn't necessary; start is fine (as you have done below)
    # Sorry Paul, what did you mean by the above comment? I get an error if I leave out int out of input

    start = int(input("Enter the start digit: "))
    # fixme: use a try...except block to catch the exception
    #  so that you don't show the user an ugly traceback
    assert start >= 0, "Start must be zero and above"
    stop = int(input("Enter the stop number: "))
    # fixme: use a try...except block here too
    assert stop > start, "Stop must be more than Start"
    step = int(input("Enter the step number: "))
    # fixme: use a try...except block here too
    assert step > 0, "Step must be 1 and above"

    print(f"Generated integers: {list(range(start, stop, step))}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
