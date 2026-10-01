from menu_item import MenuItem


class Menu:
    def __init__(self):
        self.items = {
            "B1": MenuItem("B1", "Classic Burger", 150.00),
            "B2": MenuItem("B2", "Cheeseburger", 175.00),
            "B3": MenuItem("B3", "Bacon Double", 220.00),
            "S1": MenuItem("S1", "Fries (Medium)", 65.00),
            "S2": MenuItem("S2", "Fries (Large)", 85.00),
            "D1": MenuItem("D1", "Iced Tea", 45.00),
            "D2": MenuItem("D2", "Cola", 50.00)
        }

    def get_item(self, item_id: str):
        return self.items.get(item_id.upper())

    def display(self):
        print("\n" + "=" * 45)
        print("{:^45}".format("🍔 WELCOME TO BURGER HAVEN 🍔"))
        print("=" * 45)
        print("{:<5} | {:<20} | {:<10}".format("ID", "Menu Item", "Price"))
        print("-" * 45)

        for item_id, item in self.items.items():
            print("{:<5} | {:<20} | ₱{:<10.2f}".format(item_id, item.name, item.price))
        print("=" * 45 + "\n")