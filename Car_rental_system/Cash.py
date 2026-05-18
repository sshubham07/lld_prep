from Payment import Payment
from PaymentStatus import PaymentStatus

class Cash(Payment):
    def make_payment(self):
        self.set_status(PaymentStatus.COMPLETED)
        return True