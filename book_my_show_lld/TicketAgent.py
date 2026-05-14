from Person import Person

class TicketAgent(Person):
    def create_booking(self, booking):
        print(f"Booking created by ticket agent: {self.name}")
        return True
