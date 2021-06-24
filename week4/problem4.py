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

    # Display catalogue
    for product, models in catalogue.items():
        print(f"\nProduct - {product}\n"
              f"Categories and quantities for the {product} include:\n"
              f"{'*' * 50}")
        for model, quantity in models.items():
            print(f"\t{model} - {quantity}")

    # Ask user for input
    cart = {}
    for product, models in catalogue.items():
        for model, quantity in models.items():
            print({f"Would you like to buy the {product}, {model} model?. Type Y for Yes and N for No: "})
            buy = input("Y/N: ")
            if buy == "Y" or buy == "y":
                cart[model] = int(input("Enter quantity: "))

    # Present final invoice
    if len(cart) != 0:
        print(f"Your invoice\n"
              f"===================\n "
              f"You have chosen {len(cart)} item(s)")
        for item_chosen in cart:
            print(f"\tItem: {item_chosen}, Quantity: {cart[item_chosen]}")
        print(f"Total price is KES {sum(cart.values())}")
    else:
        print("\nYou have selected no items. Try again next time")

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
