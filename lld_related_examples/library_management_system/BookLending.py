from datetime import datetime, timedelta

class BookLending:
    lendings = {}

    def __init__(self, item_id, member_id):
        self.item_id = item_id
        self.member_id = member_id
        self.creation_date = datetime.now()
        self.due_date = self.creation_date + timedelta(days=15)
        self.return_date = None
        BookLending.lendings[item_id] = self

    @staticmethod
    def lend_book(book_item_id, member_id):
        lending = BookLending(book_item_id, member_id)
        print(f"BookItem {book_item_id} lent to member {member_id}")
        return lending

    @staticmethod
    def fetch_lending_details(book_item_id):
        return BookLending.lendings.get(book_item_id)

    def get_return_date(self):
        return self.return_date
