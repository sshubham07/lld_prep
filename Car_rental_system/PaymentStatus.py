from enum import Enum

class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    CANCELED = 4
    REFUNDED = 5