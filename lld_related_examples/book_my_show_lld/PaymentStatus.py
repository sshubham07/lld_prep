from enum import Enum

class PaymentStatus(Enum):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    DECLINED = 'DECLINED'
    REFUNDED = 'REFUNDED'
