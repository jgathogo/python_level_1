import os
import sys
import math
import random

def func_1():
    return


def main():
    b = bytes("Лорем ипсум долор сит амет, меа ат неморе дицерет аппеллантур.".encode('utf-8'))
    print(b[12])

    x = random.randint(37, 92)
    print(x, 93 <= x < 137)

    b = b"\xe5\xaf\x92\xe9\xb8\xa6\xe5\x96\x9c\xe6\xac\xa2\xe6\x88\x91\xe7\x9a\x84\xe7\x9f\xb3\xe8\x8b\xb1\xe7\x8b\xae\xe8\xba\xab\xe4\xba\xba\xe9\x9d\xa2\xe5\x83\x8f\xe3\x80\x82"
    print(b.decode('utf-8'))

    # print(1723 // 13)
    # print(divmod(4, 2))
    #
    # x = 3 * 2.5
    # print(f"The value you have entered ('{x}') is incorrect!")
    #
    # t = "1,2,3,4,5,6,7,8,9,10"
    # u = t.split(",")
    # print(u, type(u))
    #
    #
    #
    # print(math.pow(2, 4))
    #
    # s = "My name is"
    # s += "Paul"
    # print(s)
    #
    #
    # """
    # Select the correct string method that allows you convert the string 'abracadabra' into '*br*c*d*br*'. *"""
    #
    # a = "abracadabra"
    # print(a.replace("a", "*"))
    #
    # x = 3908
    # e_1 = (2 * x)/(x + 1)
    # e_2 = ((9 * x**5) - (9 * x**4) - (3*x) + 3)
    # e_3 = ((9 * x**5) + (9 * x**4) - (3*x) - 3)
    #
    # print(e_1 - (e_2/e_3))
    #


    # s = "~~~~~~~~~~~~this is a string~~~~~~~~~~~"
    # print(len(s.strip("~")))
    #
    # x = 5*4
    # x *= 9
    # x /= 2
    # x += 99
    # print(x)
    #
    # x = 3 * 2.5
    # print(type(x))
    #
    # x = func_1()
    # print(x is not None)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
