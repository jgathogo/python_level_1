import os
import sys

"""
Notes:
- Very good string presentation! I can see that you spend a good deal of time on this
- The total doesn't seem to be right. Give it another shot. 
- Start with a simpler version, solve it on paper before you code, ...
"""


def main():
    catalogue = {
        'iphone': {
            'X': 800,
            'XR': 900,
            '11': 1000,
            '12': 1200,
        },
        'ipad': {
            'mini': 400,
            'air': 500,
            'pro': 800,
        },
        'mac': {
            'macbook air': 999,
            'macbook': 1299,
            'macbook pro': 1799,
        }
    }
    # Display user catalogue
    for item_d in catalogue:
        product_d = catalogue[item_d]
        print(f"\nItem - {item_d}\n"
              f"Categories and quantities for the {item_d} include:\n"
              f"++++++++++++++++")
        for category_d in product_d:
            print(f"{category_d} - {product_d[category_d]}")

    # Ask user which item they would like to purchase
    cart = {}
    for item in catalogue:
        # print(item)
        # print(catalogue[item])
        product = catalogue[item]
        print(f"Here are the {item} products: {product}")
        for category in product:
            print({f"Would you like to buy the {item}, {category} model?. Type Y for Yes and N for No: "})
            buy = input("Y/N: ")
            if buy == "Y" or buy == "y":
                cart[category] = int(input("Enter quantity: "))

    # Present final invoice
    total = 0
    if len(cart) != 0:
        print(f"Your invoice\n"
              f"===================\n "
              f"You have chosen {len(cart)} items")
        for item_chosen in cart:
            print(f"Item: {item_chosen}, Quantity: {cart[item_chosen]}")
            total += cart[item_chosen]
        print(f"Total price is KES {total}")
    else:
        print("\nYou have selected no items. Try again next time")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
