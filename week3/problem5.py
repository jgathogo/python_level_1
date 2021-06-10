import os
import sys


def main():
    print("Enter values for Matrix 1: ")
    a11 = int(input("Row 1, Column 1: "))
    a12 = int(input("Row 1, Column 2: "))
    a13 = int(input("Row 1, Column 3: "))
    a21 = int(input("Row 2, Column 1: "))
    a22 = int(input("Row 2, Column 2: "))
    a23 = int(input("Row 2, Column 3: "))
    a31 = int(input("Row 3, Column 1: "))
    a32 = int(input("Row 3, Column 2: "))
    a33 = int(input("Row 3, Column 3: "))

    print("Enter values for Matrix 2: ")
    b11 = int(input("Row 1, Column 1: "))
    b12 = int(input("Row 1, Column 2: "))
    b13 = int(input("Row 1, Column 3: "))
    b21 = int(input("Row 2, Column 1: "))
    b22 = int(input("Row 2, Column 2: "))
    b23 = int(input("Row 2, Column 3: "))
    b31 = int(input("Row 3, Column 1: "))
    b32 = int(input("Row 3, Column 2: "))
    b33 = int(input("Row 3, Column 3: "))

    a = [[a11, a12, a13],
         [a21, a22, a23],
         [a31, a32, a33]
         ]

    b = [[b11, b12, b13],
         [b21, b22, b23],
         [b31, b32, b33]
         ]

    # product matrix variables
    c11 = a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0]
    c12 = a[0][0] * b[0][1] + a[0][1] * b[1][1] + a[0][2] * b[2][1]
    c13 = a[0][0] * b[0][2] + a[0][1] * b[1][2] + a[0][2] * b[2][2]

    c21 = a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0]
    c22 = a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1]
    c23 = a[1][0] * b[0][2] + a[1][1] * b[1][2] + a[1][2] * b[2][2]

    c31 = a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0]
    c32 = a[2][0] * b[0][1] + a[2][1] * b[1][1] + a[2][2] * b[2][1]
    c33 = a[2][0] * b[0][2] + a[2][1] * b[1][2] + a[2][2] * b[2][2]

    print(f"Resulting Matrix:\n\n"
          f"{c11} {c12} {c13}\n"
          f"{c21} {c22} {c23}\n"
          f"{c31} {c32} {c33}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
