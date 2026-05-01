from typing import List
from Item import Item

class Order:
    def __init__(self, order_id: str, delivery_location: str, customer_id: str):
        self.order_id = order_id
        self.delivery_location = delivery_location
        self.customer_id = customer_id
        self.items: List[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)
