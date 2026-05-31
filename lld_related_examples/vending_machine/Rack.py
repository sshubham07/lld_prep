class Rack:
    def __init__(self, rackNumber):
        self._rackNumber = rackNumber
        self._product = None
        self._quantity = 0

    def getRackNumber(self):
        return self._rackNumber

    def isEmpty(self):
        return self._quantity <= 0

    def loadProduct(self, product, qty):
        self._product = product
        self._quantity += qty

    def peekProduct(self):
        return self._product

    def dispenseOne(self):
        if self._quantity > 0:
            self._quantity -= 1

    def __str__(self):
        if not self._product:
            return f"Rack {self._rackNumber} [empty]"
        return f"Rack {self._rackNumber}: {self._product} ×{self._quantity}"
