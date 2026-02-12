class Vehicle:
    def __init__(self, license_no):
        self.license_no = license_no
        self.ticket = None

    def assign_ticket(self, ticket):
        self.ticket = ticket
        print(f"Ticket {ticket.ticket_id} assigned to vehicle {self.license_no}")

    def remove_ticket(self):
        self.ticket = None

class Car(Vehicle):
    pass

class Van(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass
