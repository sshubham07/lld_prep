from enum import Enum

class ReservationStatus(Enum):
    WAITING = 1
    PENDING = 2
    CANCELED = 3
    NONE = 4
