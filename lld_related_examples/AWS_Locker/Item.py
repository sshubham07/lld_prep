from dataclasses import dataclass

@dataclass
class Item:
    item_id: str
    quantity: int

    def __str__(self):
        return f"Item{{itemId='{self.item_id}', quantity={self.quantity}}}"
