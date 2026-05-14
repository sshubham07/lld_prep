from enum import Enum

class BookingStatus(Enum):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'
    DENIED = 'DENIED'
    REFUNDED = 'REFUNDED'
