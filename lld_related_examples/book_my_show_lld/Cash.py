from Payment import Payment
from PaymentStatus import PaymentStatus

class Cash(Payment):
    def make_payment(self):
        print("Cash payment received.")
        self.status = PaymentStatus.CONFIRMED
        return True
