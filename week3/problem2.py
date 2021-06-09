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
    m_1 = [[1, 2],
           [3, 4]]

    m_2 = [[5, 6],
           [7, 8]]

    # compute values of the elements of the product from input matrices
    prod_r0_c0 = (m_1[0][0] * m_2[0][0]) + (m_1[0][1] * m_2[1][0])
    prod_r0_c1 = (m_1[0][0] * m_2[0][1]) + (m_1[0][1] * m_2[1][1])
    prod_r1_c0 = (m_1[1][0] * m_2[0][0]) + (m_1[1][1] * m_2[1][0])
    prod_r1_c1 = (m_1[1][0] * m_2[0][1]) + (m_1[1][1] * m_2[1][1])

    # print out resulting matrix
    print(f"{prod_r0_c0} {prod_r0_c1}\n{prod_r1_c0} {prod_r1_c1}")

    # modify program that user can input any matrix
    print("Enter values for Matrix 1: ")
    m_1_r_0_c_0 = int(input("Row 0, Column 0: "))
    m_1_r_0_c_1 = int(input("Row 0, Column 1: "))
    m_1_r_1_c_0 = int(input("Row 1, Column 0: "))
    m_1_r_1_c_1 = int(input("Row 1, Column 1: "))
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
    m_2_r_0_c_0 = int(input("Row 0, Column 0: "))
    m_2_r_0_c_1 = int(input("Row 0, Column 1: "))
    m_2_r_1_c_0 = int(input("Row 1, Column 0: "))
    m_2_r_1_c_1 = int(input("Row 1, Column 1: "))

    m_1 = [[m_1_r_0_c_0, m_1_r_0_c_1],
           [m_1_r_1_c_0, m_1_r_1_c_1]]

    print(f"Matrix 1: \n"
          f"{m_1[0][0]} {m_1[0][1]}\n{m_1[1][0]} {m_1[1][1]}")

    m_2 = [[m_2_r_0_c_0, m_2_r_0_c_1],
           [m_2_r_1_c_0, m_2_r_1_c_1]]

    print(f"Matrix 2: \n"
          f"{m_2[0][0]} {m_2[0][1]}\n{m_2[1][0]} {m_2[1][1]}")

    # This is not easy on the eyes and is very hard to double check
    prod_r0_c0 = (m_1_r_0_c_0 * m_2_r_0_c_0) + (m_1_r_0_c_1 * m_2_r_1_c_0)
    prod_r0_c1 = (m_1_r_0_c_0 * m_2_r_0_c_1) + (m_1_r_0_c_1 * m_2_r_1_c_1)
    prod_r1_c0 = (m_1_r_1_c_0 * m_2_r_0_c_0) + (m_1_r_1_c_1 * m_2_r_1_c_0)
    prod_r1_c1 = (m_1_r_1_c_0 * m_2_r_0_c_1) + (m_1_r_1_c_1 * m_2_r_1_c_1)

    m_product = [[prod_r0_c0, prod_r0_c1],
                 [prod_r1_c0, prod_r1_c1]]

    # print out resulting matrix
    print(f"Product of Matrix 1 and 2 is: \n"
          f"{m_product[0][0]} {m_product[0][1]}\n{m_product[1][0]} {m_product[1][1]}")
    # print(f"{prod_r0_c0} {prod_r0_c1}\n{prod_r1_c0} {prod_r1_c1}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
