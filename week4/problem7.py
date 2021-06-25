import os
import sys
import random


def main():
    # win = [23, 5, 48, 52, 36, 19]
    win = random.sample(range(1, 59), k=6)

    # Get input from user. First ask number of sets. Iterate by set and play.
    n_sets = int(input("Enter number of sets you would like to play. These are typically 7: "))
    d = {}
    for j in range(n_sets):
        print(f"Set {j}\n"
              f"{'=' * 20}")
        print("Enter six numbers. Each number should be between 1 and 59: ")
        bid_list = []
        for i in range(6):
            print(f"Number {i} out of 5")
            n = int(input(": "))
            bid_list.append(n)
        d[j] = bid_list

    # print(d)

    # d = {
    #     1: [3, 48, 48, 36, 19, 22],
    #     2: [23, 5, 48, 52, 36, 19],
    #     3: [23, 48, 52, 36, 19, 22]
    # }

    # Create counter dic that stores matching numbers.
    # Key for counter_d is the set number. Value is the matching numbers(list)
    counter_d = {}
    play_list = []
    for set_num, set_values in d.items():
        for play in set_values:
            if play in win:
                if play not in play_list:
                    play_list.append(play)
        counter_d[set_num] = play_list
        play_list = []

    # Choose the play list with the largest number of matching numbers.
    d_sort = {}
    for k, v in counter_d.items():
        # print(k, len(v))
        d_sort[k] = len(v)
    sorted_keys = sorted(d_sort, key=d_sort.get, reverse=True)  # sort by value i.e number of matching values
    # print(sorted_keys)

    # 'winning' list is the first in the sorted_keys list
    win_list = counter_d[sorted_keys[0]]

    criteria = {
        2: 'Free Lucky Dip',
        3: '£30',
        4: '£140',
        5: '£1,750',
        6: 'Jackpot!',
    }

    num = len(win_list)
    print(f"Win list is: {win}\n")
    if num in criteria:
        print(f"You have a match of {num}. Your win is: {criteria[num]}")
    else:
        print(f"None of the numbers you entered match the winning list. Try bidding next time."
              f"\nNumbers entered:\n{d}")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
