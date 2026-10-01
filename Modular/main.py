from menu import MENU_DICTIONARY
from display import display_menu, display_message
from order import process_order, check_discount_eligibility
from receipt import generate_and_print_receipt


def main():
    display_menu(MENU_DICTIONARY)

    start_order = input("Would you like to place an order? (yes/no): ").strip().lower()
    if start_order not in ['yes', 'y']:
        display_message("Have a great day. Exiting program...")
        return

    user_orders = process_order(MENU_DICTIONARY)

    if not user_orders:
        display_message("You didn't add anything to your cart. Exiting program...")
        return

    is_eligible = check_discount_eligibility()
    generate_and_print_receipt(user_orders, MENU_DICTIONARY, is_eligible)


if __name__ == "__main__":
    main()