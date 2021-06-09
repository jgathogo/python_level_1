import os
import sys


def main():
    print("Enter values for Matrix 1: ")
    m1_r00 = int(input("Row 0, Column 0: "))
    m1_r01 = int(input("Row 0, Column 1: "))
    m1_r02 = int(input("Row 0, Column 2: "))
    m1_r10 = int(input("Row 1, Column 0: "))
    m1_r11 = int(input("Row 1, Column 1: "))
    m1_r12 = int(input("Row 1, Column 2: "))
    m1_r20 = int(input("Row 2, Column 0: "))
    m1_r21 = int(input("Row 2, Column 1: "))
    m1_r22 = int(input("Row 2, Column 2: "))

    print("Enter values for Matrix 2: ")
    m2_r00 = int(input("Row 0, Column 0: "))
    m2_r01 = int(input("Row 0, Column 1: "))
    m2_r02 = int(input("Row 0, Column 2: "))
    m2_r10 = int(input("Row 1, Column 0: "))
    m2_r11 = int(input("Row 1, Column 1: "))
    m2_r12 = int(input("Row 1, Column 2: "))
    m2_r20 = int(input("Row 2, Column 0: "))
    m2_r21 = int(input("Row 2, Column 1: "))
    m2_r22 = int(input("Row 2, Column 2: "))

    m1 = [[m1_r00, m1_r01, m1_r02],
          [m1_r10, m1_r11, m1_r12],
          [m1_r20, m1_r21, m1_r22]
          ]

    m2 = [[m2_r00, m2_r01, m2_r02],
          [m2_r10, m2_r11, m2_r12],
          [m2_r20, m2_r21, m2_r22]
          ]

    # product matrix variables
    m_prod_r00 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0] + m1[0][2] * m2[2][0]
    m_prod_r01 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1] + m1[0][2] * m2[2][1]
    m_prod_r02 = m1[0][0] * m2[0][2] + m1[0][1] * m2[1][2] + m1[0][2] * m2[2][2]

    m_prod_r10 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0] + m1[1][2] * m2[2][0]
    m_prod_r11 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1] + m1[1][2] * m2[2][1]
    m_prod_r12 = m1[1][0] * m2[0][2] + m1[1][1] * m2[1][2] + m1[1][2] * m2[2][2]

    m_prod_r20 = m1[2][0] * m2[0][0] + m1[2][1] * m2[1][0] + m1[2][2] * m2[2][0]
    m_prod_r21 = m1[2][0] * m2[0][1] + m1[2][1] * m2[1][1] + m1[2][2] * m2[2][1]
    m_prod_r22 = m1[2][0] * m2[0][2] + m1[2][1] * m2[1][2] + m1[2][2] * m2[2][2]

    print(f"Resulting Matrix:\n\n"
          f"{m_prod_r00} {m_prod_r01} {m_prod_r02}\n"
          f"{m_prod_r10} {m_prod_r11} {m_prod_r12}\n"
          f"{m_prod_r20} {m_prod_r21} {m_prod_r22}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
