from abc import ABC, abstractmethod
from SeatStatus import SeatStatus

class Seat(ABC):
    def __init__(self):
        self.seat_no = ""
        self.status = SeatStatus.AVAILABLE

    def is_available(self):
        return self.status == SeatStatus.AVAILABLE

    @abstractmethod
    def set_seat(self):
        pass

    @abstractmethod
    def set_rate(self):
        pass
