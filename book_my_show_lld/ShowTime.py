class ShowTime:
    def __init__(self, show_id, start_time, date, duration, seats=None):
        self.show_id = show_id
        self.start_time = start_time
        self.date = date
        self.duration = duration
        self.seats = seats if seats is not None else []

    def show_available_seats(self):
        print("Available seats:")
        for seat in self.seats:
            if seat.is_available():
                print(f"Seat: {seat.seat_no}")
