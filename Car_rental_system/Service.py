from abc import ABC

class Service(ABC):
    def __init__(self):
        self._service_id = None
        self._price = 0

    def set_service_id(self, service_id): self._service_id = service_id
    def get_service_id(self): return self._service_id

    def set_price(self, price): self._price = price
    def get_price(self): return self._price