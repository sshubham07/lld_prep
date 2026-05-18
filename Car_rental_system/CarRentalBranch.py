from typing import List
from Address import Address
from ParkingStall import ParkingStall

class CarRentalBranch:
    def __init__(self, name: str, address: Address, stalls: List[ParkingStall]):
        self.name = name
        self.address = address
        self.stalls = stalls

    def get_location(self):
        return self.address

    def get_stalls(self):
        return self.stalls

    def get_name(self):
        return self.name