from Seat import Seat

class Silver(Seat):
    def __init__(self):
        super().__init__()
        self.rate = 10.0

    def set_seat(self):
        print("Silver seat set.")

    def set_rate(self):
        self.rate = 10.0
