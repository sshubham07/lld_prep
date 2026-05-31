class ParkingStall:
    def __init__(self, stall_id: int, location_identifier: str):
        self.stall_id = stall_id
        self.location_identifier = location_identifier

    def get_stall_id(self):
        return self.stall_id

    def get_location_identifier(self):
        return self.location_identifier