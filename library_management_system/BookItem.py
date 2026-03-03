from datetime import datetime, timedelta
from BookStatus import BookStatus

class BookItem:
    def __init__(self, item_id, book, placed_at, price, date_of_purchase, publication_date):
        self.id = item_id
        self.book = book
        self.is_reference_only = False
        self.borrowed = None
        self.due_date = None
        self.price = price
        self.status = BookStatus.AVAILABLE
        self.date_of_purchase = date_of_purchase
        self.publication_date = publication_date
        self.placed_at = placed_at

    def checkout(self, member_id):
        if self.status != BookStatus.AVAILABLE:
            print("BookItem not available for checkout.")
            return False
        self.status = BookStatus.LOANED
        self.borrowed = datetime.now()
        self.due_date = self.borrowed + timedelta(days=15)
        print(f"BookItem {self.id} checked out to member {member_id}. Due date: {self.due_date.date()}")
        return True

    def return_book(self):
        if self.status != BookStatus.LOANED:
            print("BookItem not loaned out.")
            return False
        self.status = BookStatus.AVAILABLE
        print(f"BookItem {self.id} returned.")
        return True

    def reserve(self):
        if self.status == BookStatus.AVAILABLE:
            self.status = BookStatus.RESERVED
            return True
        return False

    def renew(self):
        if self.status == BookStatus.LOANED:
            self.due_date += timedelta(days=15)
            print(f"BookItem {self.id} renewed. New due date: {self.due_date.date()}")
            return True
        print("Cannot renew a book that's not loaned.")
        return False
