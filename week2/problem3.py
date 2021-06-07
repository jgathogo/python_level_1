import sys
import os


def main():
    # text for question 3
    s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur rhoncus tincidunt sem nec gravida. Sed id convallis quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dui purus, ornare vitae metus vitae, feugiat ultricies ipsum. Etiam id ante quis purus rhoncus egestas. Donec vel ligula lacinia, iaculis ipsum vitae, vulputate nunc. Aliquam tellus libero, sagittis quis massa elementum, semper sodales lacus. Sed justo arcu, lobortis quis bibendum ac, fermentum ut mi. Quisque faucibus ex vitae sapien aliquam blandit. Donec fringilla sit amet augue id venenatis. Integer at nibh quis justo consectetur posuere. Nulla facilisis mi massa, sed congue lectus vehicula sed. Quisque placerat ultrices est congue vestibulum. Maecenas fermentum purus et ipsum volutpat, eu convallis risus interdum. Donec vel nunc suscipit, venenatis mi at, convallis sapien. Integer ut metus id neque rhoncus commodo."

    print(len(s))
    # a. Number of characters in the string is 920

    print(s.count("it"))
    # b. Number of 'it' occurrences is 13

    s_lower = s.lower()
    print(s_lower)
    print(s_lower.islower())  # confirm conversion
    # c. Whole text converted into lowercase

    s_i_replaced = s_lower.replace("i", "*")
    print(s_i_replaced)
    print(s_i_replaced.count("i"))  # confirm replacement
    # d. Replaced all instances of 'i' with '*'

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
