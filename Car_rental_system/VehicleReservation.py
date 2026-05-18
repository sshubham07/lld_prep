from datetime import datetime
from ReservationStatus import ReservationStatus

class VehicleReservation:
    def __init__(self):
        self._reservation_id = None
        self._customer_id = ""
        self._vehicle_id = ""
        self._creation_date = datetime.now()
        self._status = ReservationStatus.PENDING
        self._due_date = None
        self._return_date = None
        self._pickup_location = ""
        self._return_location = ""
        self._equipments = []
        self._services = []

    def set_reservation_id(self, reservation_id): self._reservation_id = reservation_id
    def get_reservation_id(self): return self._reservation_id

    def set_customer_id(self, customer_id): self._customer_id = customer_id
    def get_customer_id(self): return self._customer_id

    def set_vehicle_id(self, vehicle_id): self._vehicle_id = vehicle_id
    def get_vehicle_id(self): return self._vehicle_id

    def set_creation_date(self, date): self._creation_date = date
    def get_creation_date(self): return self._creation_date

    def set_status(self, status): self._status = status
    def get_status(self): return self._status

    def set_due_date(self, due_date): self._due_date = due_date
    def get_due_date(self): return self._due_date

    def set_return_date(self, return_date): self._return_date = return_date
    def get_return_date(self): return self._return_date

    def set_pickup_location(self, location): self._pickup_location = location
    def get_pickup_location(self): return self._pickup_location

    def set_return_location(self, location): self._return_location = location
    def get_return_location(self): return self._return_location

    def get_reservation_details(self): return self

    def add_equipment(self, equipment):
        self._equipments.append(equipment)
        return True

    def add_service(self, service):
        self._services.append(service)
        return True