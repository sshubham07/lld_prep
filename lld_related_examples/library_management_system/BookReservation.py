from datetime import datetime
from ReservationStatus import ReservationStatus

class BookReservation:
    reservations = {}

    def __init__(self, item_id, member_id):
        self.item_id = item_id
        self.creation_date = datetime.now()
        self.status = ReservationStatus.PENDING
        self.member_id = member_id
        BookReservation.reservations[item_id] = self

    @staticmethod
    def fetch_reservation_details(book_item_id):
        return BookReservation.reservations.get(book_item_id)
