import os
import random
import sys

"""
Notes:
- Great job!
- One thing to keep in mind is to be lenient to users: I find it a delightful surprise if 
the author is forgiving for innocent mistakes. For example, I want to still play even if
I have caps lock on. How can I do this?
- Instead of having a separate check to see if the user want to play on why not 
incorporate it into the choices e.g. type 'x' at any point to exit?
"""


def main():
    options = ['r', 'p', 's']
    print(f"Game rules:\n"
          f"Rock vs paper - Paper wins because rock can be wrapped in a paper\n"
          f"Rock vs scissors - Rock wins because a rock can crush a pair of scissors\n"
          f"Paper vs scissors - Scissors wins because it can cut paper\n"
          f"{'=' * 50}")

    go_on = 'y'
    while go_on != 'n':
        print("Enter option \n"
              "r for Rock\n"
              "p for Paper\n"
              "s for Scissors")

        you = input("Option: ")
        if you not in options:
            print("Run the program again and enter a valid input: ")
            # fixme: which keyword did we learn about that should be used here?
            sys.exit()

        comp = random.choice(options)
        print(f"You have entered: {you}\n"
              f"The computer has entered: {comp}\n")

        if comp == you:
            print(f"Both of you chose {comp}. Draw!")
        elif comp == 'r':
            if you == 'p':
                print("You win - paper wins because a rock can be wrapped in a paper")
            else:
                print("Computer wins - Rock wins because a rock can crush a pair of scissors")
        elif comp == 'p':
            if you == 's':
                print(f"You win - Scissors wins because it can cut paper")
            else:
                print("Computer wins - Paper wins because a rock can be wrapped in a paper")
        elif comp == 's':
            if you == 'p':
                print(f"Computer wins - scissors wins because it can cut paper")
            else:
                print(f"You win - Rock wins because a rock can crush a pair of scissors")
                # print("Run the program to play again")
        print("Do you want to continue playing? (y/n)")
        go_on = input()

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
