from abc import ABC, abstractmethod
from datetime import datetime
from PaymentStatus import PaymentStatus

class Payment(ABC):
    def __init__(self):
        self._amount = 0.0
        self._timestamp = datetime.now()
        self._status = PaymentStatus.UNPAID

    def set_amount(self, amount): self._amount = amount
    def get_amount(self): return self._amount

    def set_timestamp(self, timestamp): self._timestamp = timestamp
    def get_timestamp(self): return self._timestamp

    def set_status(self, status): self._status = status
    def get_status(self): return self._status

    @abstractmethod
    def make_payment(self): pass