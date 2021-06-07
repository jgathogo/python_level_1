import os
import sys
import random

"""
Notes
- Great discovering random.uniform. This should be the same as random.random()
- Good variable names!
- If you find time you can incorporate what we learned in Week 3 where you apply 
assertions to ensure the values entered by the user are in the right range e.g. 
if the user enters x = 1.1 the stop with a warning.
"""
def main():
    big_x = random.uniform(0, 1)
    big_y = random.uniform(0, 1)

    x = float(input("Enter value of x between 0 and 1: "))
    y = float(input("Enter value of y between 0 and 1: "))

    ace_x_lower = 0
    ace_x_upper = big_x
    ace_y_lower = big_y
    ace_y_upper = 1
    king_x_lower = big_x
    king_x_upper = 1
    king_y_lower = big_y
    king_y_upper = 1
    judge_x_lower = 0
    judge_x_upper = big_x
    judge_y_lower = 0
    judge_y_upper = big_y
    queen_x_lower = big_x
    queen_x_upper = 1
    queen_y_lower = big_x
    queen_y_upper = big_y

    # check if x or y is between X/Y
    ace_check = (ace_x_lower <= x <= ace_x_upper) and (ace_y_lower <= y <= ace_y_upper)
    king_check = (king_x_lower <= x <= king_x_upper) and (king_y_lower <= y <= king_y_upper)
    judge_check = (judge_x_lower <= x <= judge_x_upper) and (judge_y_lower <= y <= judge_y_upper)
    queen_check = (queen_x_lower <= x <= queen_x_upper) and (queen_y_lower <= y <= queen_y_upper)

    print(f"X: {big_x}, Y: {big_y}, x: {x}, y: {y}")

    print(f"Ace: {ace_check}")
    print(f"King: {king_check}")
    print(f"Judge: {judge_check}")
    print(f"Queen: {queen_check}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
