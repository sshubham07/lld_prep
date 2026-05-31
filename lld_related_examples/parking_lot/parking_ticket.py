class ParkingTicket:
    def __init__(self,ticket_id, vehicle, spot):
        self.ticket_id = ticket_id
        self.entry_time = None
        self.exit_time = None
        self.amount = None
        self.status = None  # type: TicketStatus

        self.vehicle = vehicle
        self.payment = None  # type: Payment
        self.entrance = None
        self.exit_ins = None
        self.spot = spot