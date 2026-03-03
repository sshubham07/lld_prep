from datetime import datetime

class LibraryCard:
    def __init__(self, card_number, issued):
        self.card_number = card_number
        self.issued = issued
        self.active = True

    def is_active(self):
        return self.active
