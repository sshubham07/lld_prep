from Catalog import Catalog

class Library:
    _instance = None

    def __init__(self, name, address):
        if Library._instance is not None:
            raise Exception("This class is a singleton!")
        self.name = name
        self.address = address
        self.catalog = Catalog()
        Library._instance = self

    @staticmethod
    def get_instance(name, address):
        if Library._instance is None:
            Library(name, address)
        return Library._instance

    def get_address(self):
        return str(self.address)
