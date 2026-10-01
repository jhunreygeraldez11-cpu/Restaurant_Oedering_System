from menu import Menu
from order import Order
from receipt import Receipt


class BurgerHavenApp:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    @staticmethod
    def display_message(message: str):
        print(f"> {message}")

    def run(self):
        self.menu.display()

        start_order = input("Would you like to place an order? (yes/no): ").strip().lower()
        if start_order not in ['yes', 'y']:
            self.display_message("Have a great day. Exiting program...")
            return

        is_ordering = True
        while is_ordering:
            item_id = input("\nEnter the ID of the item you want to order: ").strip().upper()
            item = self.menu.get_item(item_id)

            if not item:
                self.display_message("Error: Invalid Menu ID. Please check the menu and try again.")
                continue

            try:
                qty_input = int(input(f"How many '{item.name}' would you like? "))
                if qty_input <= 0:
                    self.display_message("Error: Quantity must be 1 or more.")
                    continue
            except ValueError:
                self.display_message("Error: Please enter a valid number for the quantity.")
                continue

            self.order.add_item(item, qty_input)
            self.display_message(f"Successfully added {qty_input}x {item.name} to cart.")

            while True:
                order_again = input("\nWould you like to order another item? (yes/no): ").strip().lower()
                if order_again in ['yes', 'y', 'no', 'n']:
                    break
                self.display_message("Invalid response. Please answer 'yes' or 'no'.")

            if order_again in ['no', 'n']:
                is_ordering = False

        if self.order.is_empty():
            self.display_message("You didn't add anything to your cart. Exiting program...")
            return

        while True:
            discount_input = input("\nAre you eligible for a 20% Senior Citizen / PWD discount? (yes/no): ").strip().lower()
            if discount_input in ['yes', 'y', 'no', 'n']:
                self.order.apply_discount = discount_input in ['yes', 'y']
                break
            self.display_message("Invalid response. Please answer 'yes' or 'no'.")

        receipt = Receipt(self.order)
        receipt.print_receipt()


if __name__ == "__main__":
    app = BurgerHavenApp()
    app.run()