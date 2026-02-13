import math
class DisplayBoard:
    def __init__(self,id):
        self.id = id
        self.parking_spots = None  # dict: str -> list of ParkingSpot

    # def add_parking_spot(self, spot_type, spots):
    #     pass

    def show_free_slot(self,spots):
        print(f"\nDisplayBoard {self.id} Status:")
        free_count = {}
        for spot in spots:
            spot_type = spot.__class__.__name__

            if spot_type not in free_count:
                free_count[spot_type] = 0

            if spot.is_free():
                free_count[spot_type] += 1

        for spot_type, count in free_count.items():
            print(f"{spot_type}: {count} free spots")

class ParkingRate:
    def __init__(self):
        # Hourly rate per vehicle type
        self.rates = {
            "Car": 10,
            "Van": 15,
            "Truck": 20,
            "Motorcycle": 5
        }

    def calculate(self, duration, vehicle, spot):
        # Round up to next hour
        hours = math.ceil(duration)

        vehicle_type = vehicle.__class__.__name__

        rate_per_hour = self.rates.get(vehicle_type, 10)

        total_amount = hours * rate_per_hour

        return total_amount