from menu_item import MenuItem
from order_item import OrderItem


class Order:
    def __init__(self):
        self.items = []
        self.apply_discount = False

    def add_item(self, item: MenuItem, quantity: int):
        for order_item in self.items:
            if order_item.item.item_id == item.item_id:
                order_item.quantity += quantity
                return
        self.items.append(OrderItem(item, quantity))

    def calculate_subtotal(self) -> float:
        return sum(item.get_total() for item in self.items)

    def calculate_discount(self) -> float:
        if self.apply_discount:
            return self.calculate_subtotal() * 0.20
        return 0.0

    def calculate_grand_total(self) -> float:
        return self.calculate_subtotal() - self.calculate_discount()

    def is_empty(self) -> bool:
        return len(self.items) == 0