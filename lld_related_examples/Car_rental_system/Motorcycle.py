from vehicle import Vehicle
from MotorcycleType import MotorcycleType

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
        self._motorcycle_type = None

    def get_motorcycle_type(self):
        return self._motorcycle_type

    def set_motorcycle_type(self, motorcycle_type: MotorcycleType):
        self._motorcycle_type = motorcycle_type