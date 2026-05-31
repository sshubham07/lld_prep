from parking_ticket import ParkingTicket
import time
import uuid
from parking_lot import ParkingLot
from display import ParkingRate
import datetime
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
                ticket.entry_time = datetime.datetime.now()

                # Save ticket in lot
                lot.tickets[ticket_id] = ticket

                # Assign ticket to vehicle
                vehicle.assign_ticket(ticket)

                print(f"Ticket issued: {ticket_id}")
                return ticket

        print("Parking Lot is Full or no suitable spot available.")
        return None

class Exit:
    def __init__(self, id):
        self.id = id
        self.rate_calculator = ParkingRate()

    def validate_ticket(self, ticket):
        if ticket is None:
            print("Invalid ticket.")
            return

        lot = ParkingLot.get_instance()

        # Set exit time
        ticket.exit_time = datetime.datetime.now()

        # Calculate duration in hours
        duration_seconds = (ticket.exit_time - ticket.entry_time).total_seconds()
        duration_hours = duration_seconds / 3600

        # Calculate amount
        amount = self.rate_calculator.calculate(duration_hours, ticket.vehicle, ticket.spot)

        print(f"Parking duration: {round(duration_hours, 2)} hours")
        print(f"Total amount to pay: {amount}")

        # Free the spot
        ticket.spot.remove_vehicle()

        # Remove ticket from vehicle
        ticket.vehicle.remove_ticket()

        # Remove ticket from lot records
        if ticket.ticket_id in lot.tickets:
            del lot.tickets[ticket.ticket_id]

        print(f"Ticket {ticket.ticket_id} closed successfully.")

        return amount