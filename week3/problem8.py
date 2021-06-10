import os
import sys


def main():
    # no need for int_* in the variable name
    # Sorry Paul, what did you mean by the above comment? I get an error if I leave out int out of input

    start = int(input("Enter the start digit: "))
    assert start >= 0, "Start must be zero and above"
    stop = int(input("Enter the stop number: "))
    assert stop > start, "Stop must be more than Start"
    step = int(input("Enter the step number: "))
    assert step > 0, "Step must be 1 and above"

    print(f"Generated integers: {list(range(start, stop, step))}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
