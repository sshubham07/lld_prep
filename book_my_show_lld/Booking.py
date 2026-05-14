class Booking:
    def __init__(self, booking_id, amount, total_seats, created_on, status, payment, tickets, seats):
        self.booking_id = booking_id
        self.amount = amount
        self.total_seats = total_seats
        self.created_on = created_on
        self.status = status
        self.payment = payment
        self.tickets = tickets
        self.seats = seats
