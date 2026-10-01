def display_message(message):
    print(f"> {message}")


def display_menu(menu_dict):
    print("\n" + "=" * 45)
    print("{:^45}".format("🍔 WELCOME TO BURGER HAVEN 🍔"))
    print("=" * 45)
    print("{:<5} | {:<20} | {:<10}".format("ID", "Menu Item", "Price"))
    print("-" * 45)

    for item_id, details in menu_dict.items():
        print("{:<5} | {:<20} | ₱{:<10.2f}".format(item_id, details['name'], details['price']))
    print("=" * 45 + "\n")