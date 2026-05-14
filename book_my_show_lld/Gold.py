from Seat import Seat

class Gold(Seat):
    def __init__(self):
        super().__init__()
        self.rate = 12.0

    def set_seat(self):
        print("Gold seat set.")

    def set_rate(self):
        self.rate = 12.0
