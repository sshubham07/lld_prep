class Fine:
    def __init__(self):
        self._amount = 0.0
        self._reason = ""

    def set_amount(self, amount):
        self._amount = amount

    def get_amount(self):
        return self._amount

    def set_reason(self, reason):
        self._reason = reason

    def get_reason(self):
        return self._reason

    def calculate_fine(self):
        return self._amount