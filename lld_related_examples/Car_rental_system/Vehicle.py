from abc import ABC
from VehicleStatus import VehicleStatus
from VehicleLog import VehicleLog

class Vehicle(ABC):
    def __init__(self):
        self._vehicle_id = ""
        self._license_plate_number = ""
        self._passenger_capacity = 0
        self._has_sunroof = False
        self._status = VehicleStatus.AVAILABLE
        self._model = ""
        self._manufacturing_year = 0
        self._mileage = 0
        self._log = []

    def get_vehicle_id(self): return self._vehicle_id
    def set_vehicle_id(self, vehicle_id): self._vehicle_id = vehicle_id

    def set_model(self, model): self._model = model
    def get_model(self): return self._model

    def set_manufacturing_year(self, year): self._manufacturing_year = year
    def get_manufacturing_year(self): return self._manufacturing_year

    def set_status(self, status): self._status = status
    def get_status(self): return self._status

    def reserve_vehicle(self):
        if self._status == VehicleStatus.AVAILABLE:
            self._status = VehicleStatus.RESERVED
            return True
        return False

    def return_vehicle(self):
        if self._status == VehicleStatus.RESERVED:
            self._status = VehicleStatus.AVAILABLE
            return True
        return False