from datetime import datetime
from User import User
from Fine import Fine

class Member(User):
    def __init__(self, user_id, password, person, card):
        super().__init__(user_id, password, person, card)
        self.date_of_membership = datetime.now()
        self.total_books_checked_out = 0
        self.books_borrowed = []
        self.fines_due = 0.0

    def reserve_book_item(self, book_item):
        if book_item.reserve():
            print(f"BookItem {book_item.id} reserved by member {self.id}")
            return True
        print("Cannot reserve book; it is not available.")
        return False

    def checkout_book_item(self, book_item):
        if self.total_books_checked_out >= 10:
            print("Book limit reached.")
            return False
        if book_item.checkout(self.id):
            self.books_borrowed.append(book_item)
            self.total_books_checked_out += 1
            print(f"Member {self.id} checked out BookItem {book_item.id}")
            return True
        return False

    def return_book_item(self, book_item):
        if book_item not in self.books_borrowed:
            print("Book not checked out by member.")
            return False

        late_days = 0
        if book_item.due_date:
            diff = datetime.now() - book_item.due_date
            late_days = max(0, diff.days)

        if late_days > 0:
            fine = Fine.collect_fine(self.id, late_days)
            self.fines_due += fine
            print(f"Fine of ${fine:.2f} applied for {late_days} late days.")

        book_item.return_book()
        self.books_borrowed.remove(book_item)
        self.total_books_checked_out -= 1
        return True

    def renew_book_item(self, book_item):
        if book_item in self.books_borrowed:
            return book_item.renew()
        print("This member has not checked out the book.")
        return False

    def reset_password(self):
        print(f"Reset password for user {self.id}")
        return True
