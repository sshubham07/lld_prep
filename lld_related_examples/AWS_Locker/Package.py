from Order import Order

class Package:
    def __init__(self, package_id: str, package_size: float, order: Order):
        self.package_id = package_id
        self.package_size = package_size
        self.order = order

    def pack(self):
        print(f"Packing package {self.package_id} for order {self.order.order_id}")
