from enum import Enum

class ReservationStatus(Enum):
    ACTIVE = 1
    PENDING = 2
    CONFIRMED = 3
    COMPLETED = 4
    CANCELED = 5