import os
import sys

"""
Notes
- trivial point: instead of using bulky variable names you can
use A for the matrix name and a11,a12,... for the element names; 
intricate variable names are more liable to bugs
- Nice string formatting!
"""


def main():
    # hard-code input matrices
    x = [[1, 2],
         [3, 4]]

    y = [[5, 6],
         [7, 8]]

    # compute values of the elements of the product from input matrices
    z11 = (x[0][0] * y[0][0]) + (x[0][1] * y[1][0])
    z12 = (x[0][0] * y[0][1]) + (x[0][1] * y[1][1])
    z21 = (x[1][0] * y[0][0]) + (x[1][1] * y[1][0])
    z22 = (x[1][0] * y[0][1]) + (x[1][1] * y[1][1])

    # print out resulting matrix
    print(f"{z11} {z12}\n{z21} {z22}")

    # modify program that user can input any matrix
    print("Enter values for Matrix 1: ")
    a11 = int(input("Row 1, Column 1: "))
    a12 = int(input("Row 1, Column 2: "))
    a21 = int(input("Row 2, Column 1: "))
    a22 = int(input("Row 2, Column 2: "))
    """
    # For example the above could be simplified to
    a11 = int(input("a11: "))
    a12 = int(input("a12: "))
    a21 = int(input("a21: "))
    a22 = int(input("a22: "))
    A = [[a11, a12], [a21, a22]]
    # Does that look cleaner?
    # As a programmer, you will spend a lot more time reading code than
    # writing it
    """

    print("Enter values for Matrix 2: ")
    b11 = int(input("Row 1, Column 1: "))
    b12 = int(input("Row 1, Column 2: "))
    b21 = int(input("Row 2, Column 1: "))
    b22 = int(input("Row 2, Column 2: "))

    a = [[a11, a12],
         [a21, a22]]

    print(f"Matrix 1: \n"
          f"{a[0][0]} {a[0][1]}\n{a[1][0]} {a[1][1]}")

    b = [[b11, b12],
         [b21, b22]]

    print(f"Matrix 2: \n"
          f"{b[0][0]} {b[0][1]}\n{b[1][0]} {b[1][1]}")

    # This is not easy on the eyes and is very hard to double check
    c11 = (a11 * b11) + (a12 * b21)
    c12 = (a11 * b12) + (a12 * b22)
    c21 = (a21 * b11) + (a22 * b21)
    c22 = (a21 * b12) + (a22 * b22)

    c = [[c11, c12],
         [c21, c22]]

    # print out resulting matrix
    print(f"Product of Matrix 1 and 2 is: \n"
          f"{c[0][0]} {c[0][1]}\n{c[1][0]} {c[1][1]}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
