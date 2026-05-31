from Person import Person

class Customer(Person):
    def __init__(self):
        super().__init__()
        self.bookings = []

    def create_booking(self, booking):
        self.bookings.append(booking)
        print(f"Booking created by customer: {self.name}")
        return True

    def update_booking(self, booking):
        print(f"Booking updated by customer: {self.name}")
        return True

    def delete_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)
        print(f"Booking deleted by customer: {self.name}")
        return True
