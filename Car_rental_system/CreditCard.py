from Payment import Payment
from PaymentStatus import PaymentStatus

class CreditCard(Payment):
    def __init__(self):
        super().__init__()
        self.name_on_card = ""
        self.card_number = ""
        self.billing_address = ""
        self.code = 0

    def set_name_on_card(self, name):
        self.name_on_card = name

    def set_card_number(self, number):
        self.card_number = number

    def set_billing_address(self, address):
        self.billing_address = address

    def set_code(self, code):
        self.code = code

    def make_payment(self):
        self.set_status(PaymentStatus.COMPLETED)
        return True