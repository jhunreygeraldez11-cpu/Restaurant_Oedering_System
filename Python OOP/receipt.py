from order import Order


class Receipt:
    def __init__(self, order: Order):
        self.order = order

    def print_receipt(self):
        print("\n\n" + "=" * 50)
        print("{:^50}".format("BURGER HAVEN - OFFICIAL RECEIPT"))
        print("=" * 50)
        print("{:<4} | {:<18} | {:<8} | {:<10}".format("QTY", "ITEM", "@PRICE", "TOTAL"))
        print("-" * 50)

        for order_item in self.order.items:
            qty = order_item.quantity
            name = order_item.item.name
            price = order_item.item.price
            line_total = order_item.get_total()

            print("{:<4} | {:<18} | ₱{:<7.2f} | ₱{:<9.2f}".format(qty, name[:18], price, line_total))

        subtotal = self.order.calculate_subtotal()
        discount = self.order.calculate_discount()
        grand_total = self.order.calculate_grand_total()

        print("-" * 50)
        print("{:<36} ₱{:<9.2f}".format("SUBTOTAL:", subtotal))

        if self.order.apply_discount:
            print("{:<36} -₱{:<9.2f}".format("DISCOUNT (20%):", discount))

        print("=" * 50)
        print("{:<36} ₱{:<9.2f}".format("GRAND TOTAL:", grand_total))
        print("=" * 50)
        print("{:^50}".format("Thank you for dining with us!"))
        print("{:^50}".format("Please come again."))
        print("=" * 50 + "\n")