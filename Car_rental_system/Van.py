from Vehicle import Vehicle
from VanType import VanType

class Van(Vehicle):
    def __init__(self):
        super().__init__()
        self._van_type = None

    def get_van_type(self):
        return self._van_type

    def set_van_type(self, van_type: VanType):
        self._van_type = van_type