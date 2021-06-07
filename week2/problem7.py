import os
import sys

"""
Notes
- width would be a good candidate for a variable; only update one place
- no need to use title case for the url
- string methods can be chained e.g. "text".center(100).title()
- It is good practice (in my book) to run 'Reformat Code' periodically. It will become 
evident that you need to clean your code because PyCharm will add squiggles to your
code. Go to Code > Reformat Code or simply use the shortcut shown periodically. It 
might even be possible to have this run automatically. Ideally, you're aiming to 
have a green check mark in the top right corner.
"""


def main():
    width = 50
    line_1 = "apache license".center(width, " ")
    line_2 = "version 2.0, january 2004".center(width, " ")
    line_3 = "http://www.apache.org/licenses/".center(width, " ")
    print(line_1.title())
    print(line_2.title())
    print(line_3.title())  # this is not correct; no need for title

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
