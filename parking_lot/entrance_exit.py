from parking_ticket import ParkingTicket
import time
import uuid
from parking_lot import ParkingLot
class Entrance:
    def __init__(self,id):
        self.id = id

    def get_ticket(self, vehicle):
        lot = ParkingLot.get_instance()

        # Find suitable spot
        for spot in lot.spots.values():
            if spot.is_free() and spot.can_fit_vehicle(vehicle):

                # Assign vehicle to spot
                spot.assign_vehicle(vehicle)

                # Generate ticket
                ticket_id = str(uuid.uuid4())
                ticket = ParkingTicket(ticket_id, vehicle, spot)

                # Save ticket in lot
                lot.tickets[ticket_id] = ticket

                # Assign ticket to vehicle
                vehicle.assign_ticket(ticket)

                print(f"Ticket issued: {ticket_id}")
                return ticket

        print("Parking Lot is Full or no suitable spot available.")
        return None

class Exit:
    def __init__(self,id):
        self.id = id

    def validate_ticket(self, ticket):
        pass