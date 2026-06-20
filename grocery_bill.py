"""
Grocery Bill Generator
------------------------
A simple command-line program that asks you to enter grocery items one by one,
then prints a final bill with the total amount.

Run this directly in PyCharm (right-click -> Run, or press the green play button).
"""

from datetime import datetime

# This list will store every item added during the session.
# Each item is stored as a dictionary: {"name": ..., "qty": ..., "price": ..., "total": ...}
cart = []


def add_item():
    """Ask the user for one grocery item and add it to the cart."""
    print("\n--- Add Grocery Item ---")

    name = input("Item name (e.g. Rice, Milk, Sugar): ").strip()
    while not name:
        name = input("Item name cannot be empty. Try again: ").strip()

    # Ask for quantity, keep asking until a valid positive number is entered
    qty = None
    while qty is None:
        raw_qty = input(f"Quantity of '{name}': ").strip()
        try:
            qty = float(raw_qty)
            if qty <= 0:
                print("Quantity must be greater than 0.")
                qty = None
        except ValueError:
            print("Please enter a valid number.")

    # Ask for price per unit, keep asking until valid
    price = None
    while price is None:
        raw_price = input(f"Price per unit of '{name}' (Rs.): ").strip()
        try:
            price = float(raw_price)
            if price <= 0:
                print("Price must be greater than 0.")
                price = None
        except ValueError:
            print("Please enter a valid number.")

    item_total = qty * price

    cart.append({
        "name": name,
        "qty": qty,
        "price": price,
        "total": item_total
    })

    print(f"✔ Added: {name} — {qty} x Rs. {price:,.0f} = Rs. {item_total:,.0f}")


def show_cart():
    """Show all items currently in the cart, without totals/bill formatting."""
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n--- Current Cart ---")
    print(f"{'#':<4}{'Item':<18}{'Qty':<8}{'Price':<12}{'Total':<12}")
    print("-" * 54)
    for i, item in enumerate(cart, start=1):
        print(f"{i:<4}{item['name']:<18}{item['qty']:<8.2f}{'Rs. ' + format(item['price'], ',.0f'):<12}{'Rs. ' + format(item['total'], ',.0f'):<12}")


def remove_item():
    """Remove an item from the cart by its number."""
    if not cart:
        print("\nCart is empty, nothing to remove.")
        return

    show_cart()
    raw = input("\nEnter the # of the item to remove (or 0 to cancel): ").strip()

    try:
        index = int(raw)
    except ValueError:
        print("Invalid input.")
        return

    if index == 0:
        print("Cancelled.")
        return

    if 1 <= index <= len(cart):
        removed = cart.pop(index - 1)
        print(f"✔ Removed: {removed['name']}")
    else:
        print("That item number doesn't exist.")


def print_final_bill():
    """Print a formatted final bill/receipt with grand total."""
    if not cart:
        print("\nCart is empty. Add some items before printing the bill.")
        return

    grand_total = sum(item["total"] for item in cart)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print("\n" + "=" * 46)
    print("           GROCERY BILL / RECEIPT")
    print("=" * 46)
    print(f"Date: {now}")
    print("-" * 46)
    print(f"{'Item':<16}{'Qty':<8}{'Price':<10}{'Total':>12}")
    print("-" * 46)

    for item in cart:
        print(f"{item['name']:<16}{item['qty']:<8.2f}{format(item['price'], ',.0f'):<10}{format(item['total'], ',.0f'):>12}")

    print("-" * 46)
    print(f"{'GRAND TOTAL':<34}{'Rs. ' + format(grand_total, ',.0f'):>12}")
    print("=" * 46)
    print(f"Total items: {len(cart)}")
    print("Thank you!\n")


def print_menu():
    print("\n" + "=" * 40)
    print("        GROCERY BILL GENERATOR")
    print("=" * 40)
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Remove an item")
    print("4. Print final bill")
    print("5. Exit")


def main():
    print("Welcome! Let's build your grocery bill.")

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            show_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print_final_bill()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
