class DisplayBoard:
    def __init__(self,id):
        self.id = id
        self.parking_spots = None  # dict: str -> list of ParkingSpot

    def add_parking_spot(self, spot_type, spots):
        pass

    def show_free_slot(self):
        pass

    def update(self,spots):
        pass

class ParkingRate:
    def __init__(self):
        self.hours = None
        self.rate = None

    def calculate(self, duration, vehicle, spot):
        pass