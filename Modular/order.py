from display import display_message


def process_order(menu_dict):
    user_orders = []
    is_ordering = True

    while is_ordering:
        item_input = input("\nEnter the ID of the item you want to order: ").strip().upper()

        if item_input not in menu_dict:
            display_message("Error: Invalid Menu ID. Please check the menu and try again.")
            continue

        try:
            qty_input = int(input(f"How many '{menu_dict[item_input]['name']}' would you like? "))

            if qty_input <= 0:
                display_message("Error: Quantity must be 1 or more.")
                continue

        except ValueError:
            display_message("Error: Please enter a valid number for the quantity.")
            continue

        item_exists = False
        for order in user_orders:
            if order['id'] == item_input:
                order['qty'] += qty_input
                item_exists = True
                break

        if not item_exists:
            user_orders.append({'id': item_input, 'qty': qty_input})

        display_message(f"Successfully added {qty_input}x {menu_dict[item_input]['name']} to cart.")

        while True:
            order_again = input("\nWould you like to order another item? (yes/no): ").strip().lower()
            if order_again in ['yes', 'y', 'no', 'n']:
                break
            display_message("Invalid response. Please answer 'yes' or 'no'.")

        if order_again in ['no', 'n']:
            is_ordering = False

    return user_orders


def check_discount_eligibility():
    while True:
        discount_input = input("\nAre you eligible for a 20% Senior Citizen / PWD discount? (yes/no): ").strip().lower()
        if discount_input in ['yes', 'y', 'no', 'n']:
            return discount_input in ['yes', 'y']
        display_message("Invalid response. Please answer 'yes' or 'no'.")