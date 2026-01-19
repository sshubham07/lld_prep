class ParkingSpot:
    def __init__(self,id):
        self.id = id
        self.is_free = None
        self.vehicle = None  # type: Vehicle

    def assign_vehicle(self, vehicle):
        pass

    def remove_vehicle(self):
        pass

class Accessible(ParkingSpot):
    def assign_vehicle(self, vehicle):
        pass

class Compact(ParkingSpot):
    def assign_vehicle(self, vehicle):
        pass

class Large(ParkingSpot):
    def assign_vehicle(self, vehicle):
        pass

class MotorcycleSpot(ParkingSpot):
    def assign_vehicle(self, vehicle):
        pass