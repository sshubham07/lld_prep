from abc import ABC

class Equipment(ABC):
    def __init__(self):
        self._equipment_id = None
        self._price = 0

    def set_equipment_id(self, equipment_id): self._equipment_id = equipment_id
    def get_equipment_id(self): return self._equipment_id

    def set_price(self, price): self._price = price
    def get_price(self): return self._price