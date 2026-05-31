from Vehicle import Vehicle
from CarType import CarType

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._car_type = None

    def get_car_type(self):
        return self._car_type

    def set_car_type(self, car_type: CarType):
        self._car_type = car_type