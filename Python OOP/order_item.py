from menu_item import MenuItem


class OrderItem:
    def __init__(self, item: MenuItem, quantity: int):
        self.item = item
        self.quantity = quantity

    def get_total(self) -> float:
        return self.item.price * self.quantity