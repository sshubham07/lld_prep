from Vehicle import Vehicle
from TruckType import TruckType

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self._truck_type = None

    def get_truck_type(self):
        return self._truck_type

    def set_truck_type(self, truck_type: TruckType):
        self._truck_type = truck_type