from Seat import Seat

class Platinum(Seat):
    def __init__(self):
        super().__init__()
        self.rate = 15.0

    def set_seat(self):
        print("Platinum seat set.")

    def set_rate(self):
        self.rate = 15.0
