class Vehicle:
    def __init__(self,license_no):
        self.license_no = license_no
        self.ticket = None  # type: ParkingTicket

    def assign_ticket(self, ticket):
        pass

class Car(Vehicle):
    def assign_ticket(self, ticket):
        pass

class Van(Vehicle):
    def assign_ticket(self, ticket):
        pass

class Truck(Vehicle):
    def assign_ticket(self, ticket):
        pass

class Motorcycle(Vehicle):
    def assign_ticket(self, ticket):
        pass