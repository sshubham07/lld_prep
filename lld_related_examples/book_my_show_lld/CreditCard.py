from Payment import Payment
from PaymentStatus import PaymentStatus

class CreditCard(Payment):
    def __init__(self):
        super().__init__()
        self.name_on_card = ""
        self.card_number = ""
        self.billing_address = ""
        self.code = 0

    def make_payment(self):
        print(f"Credit card payment processed for {self.name_on_card}")
        self.status = PaymentStatus.CONFIRMED
        return True
