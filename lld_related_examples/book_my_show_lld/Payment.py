from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self):
        self.amount = 0.0
        self.timestamp = None
        self.status = None

    @abstractmethod
    def make_payment(self):
        pass
