from User import User
from AccountStatus import AccountStatus

class Librarian(User):
    def reset_password(self):
        print(f"Reset password for user {self.id}")
        return True

    def add_book_item(self, catalog, book_item):
        catalog.add_book_item(book_item)
        print(f"BookItem {book_item.id} added to catalog by librarian {self.id}")
        return True

    def block_member(self, member):
        member.status = AccountStatus.BLACKLISTED
        print(f"Member {member.id} is now blacklisted.")
        return True

    def un_block_member(self, member):
        member.status = AccountStatus.ACTIVE
        print(f"Member {member.id} is now active.")
        return True
