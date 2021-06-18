import os
import sys

"""
Notes/Questions:
- Excellent solution! You only forgot to print out d!
- How may we simplify the following using what we have learned so far? 

    d[i] = d[i] + 1
    
- Please make you code more compact; fewer blank lines
- If the user does not follow instructions the program should halt. 
How would you implement this? I think sys.exit()
"""


def main():
    text = input("Enter a ten character word: ")
    if len(text) != 10:
        print("Number of characters should be exactly 10 in number.\n"
              "Please run the program again and enter exactly 10 characters")
        sys.exit()
    d = {}
    for i in text:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    print(d)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
