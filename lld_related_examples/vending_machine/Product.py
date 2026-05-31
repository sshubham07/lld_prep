class Product:
    def __init__(self, id, name, price, type_):
        self._id = id
        self._name = name
        self._price = price
        self._type = type_

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getPrice(self):
        return self._price

    def getType(self):
        return self._type

    def __str__(self):
        return f"{self._name} (id={self._id}) @ ${self._price:.2f}"
