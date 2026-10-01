def generate_and_print_receipt(order_list, menu_dict, apply_discount):
    print("\n\n" + "=" * 50)
    print("{:^50}".format("BURGER HAVEN - OFFICIAL RECEIPT"))
    print("=" * 50)
    print("{:<4} | {:<18} | {:<8} | {:<10}".format("QTY", "ITEM", "@PRICE", "TOTAL"))
    print("-" * 50)

    subtotal = 0.0

    for order in order_list:
        item_id = order['id']
        qty = order['qty']
        name = menu_dict[item_id]['name']
        price = menu_dict[item_id]['price']

        line_total = price * qty
        subtotal += line_total

        print("{:<4} | {:<18} | ₱{:<7.2f} | ₱{:<9.2f}".format(qty, name[:18], price, line_total))

    print("-" * 50)
    print("{:<36} ₱{:<9.2f}".format("SUBTOTAL:", subtotal))

    discount_amount = 0.0
    if apply_discount:
        discount_amount = subtotal * 0.20
        print("{:<36} -₱{:<9.2f}".format("DISCOUNT (20%):", discount_amount))

    grand_total = subtotal - discount_amount

    print("=" * 50)
    print("{:<36} ₱{:<9.2f}".format("GRAND TOTAL:", grand_total))
    print("=" * 50)
    print("{:^50}".format("Thank you for dining with us!"))
    print("{:^50}".format("Please come again."))
    print("=" * 50 + "\n")