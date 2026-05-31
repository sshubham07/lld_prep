from vehicle import Car, Van, Truck, Motorcycle
class ParkingSpot:
    def __init__(self,id):
        self.id = id
        self._is_free = True
        self.vehicle = None  # type: Vehicle
    
    def is_free(self):
        return self._is_free

    def assign_vehicle(self, vehicle):
        if not self._is_free:
            print(f"Spot {self.id} is already occupied.")
            return False

        self._is_free = False
        self.vehicle = vehicle
        print(f"{vehicle.license_no} parked at Spot {self.id}")
        return True

    def remove_vehicle(self):
        if self._is_free:
            print(f"Spot {self.id} is already empty.")
            return None

        self._is_free = True
        vehicle = self.vehicle
        self.vehicle = None
        print(f"{vehicle.license_no} left Spot {self.id}")
        return vehicle
    def can_fit_vehicle(self, vehicle):
        # Base class allows everything (override in child classes)
        return True

class Accessible(ParkingSpot):
    def can_fit_vehicle(self, vehicle):
        return isinstance(vehicle, (Motorcycle, Car, Van))

class Compact(ParkingSpot):
    def can_fit_vehicle(self, vehicle):
        return isinstance(vehicle, (Motorcycle, Car))

class Large(ParkingSpot):
    def can_fit_vehicle(self, vehicle):
        return isinstance(vehicle, (Motorcycle, Car, Van, Truck))

class MotorcycleSpot(ParkingSpot):
    def can_fit_vehicle(self, vehicle):
        return isinstance(vehicle, Motorcycle)