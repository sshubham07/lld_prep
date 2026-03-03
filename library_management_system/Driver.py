from datetime import datetime, timedelta
from Address import Address
from Author import Author
from Book import Book
from BookFormat import BookFormat
from Rack import Rack
from BookItem import BookItem
from Library import Library
from LibraryCard import LibraryCard
from Person import Person
from Member import Member
from Librarian import Librarian
from EmailNotification import EmailNotification
from PostalNotification import PostalNotification

if __name__ == "__main__":
    try:
        print("\n========== SYSTEM INITIALIZATION ==========\n")
        lib_address = Address("1 Main St", "Springfield", "State", 12345, "Country")
        library = Library.get_instance("Springfield Public Library", lib_address)

        # Authors
        author1 = Author("Jane Austen", lib_address, "austen@email.com", "123456", "Famous novelist")
        author2 = Author("Mark Twain", lib_address, "twain@email.com", "234567", "Another novelist")

        # Books and BookItems
        pub_date1 = datetime.strptime("2000-01-01", "%Y-%m-%d")
        pub_date2 = datetime.strptime("2005-05-20", "%Y-%m-%d")
        book1 = Book("ISBN123", "Pride and Prejudice", "Novel", "Publisher A",
                     pub_date1, "English", 300, BookFormat.HARDCOVER, [author1])
        book2 = Book("ISBN456", "Adventures of Huckleberry Finn", "Adventure", "Publisher B",
                     pub_date2, "English", 250, BookFormat.PAPERBACK, [author2])
        rack1 = Rack(1, "A1")
        rack2 = Rack(2, "B2")
        book_item1 = BookItem("BI001", book1, rack1, 30.0, datetime.strptime("2020-01-01", "%Y-%m-%d"), book1.publication_date)
        book_item2 = BookItem("BI002", book2, rack2, 25.0, datetime.strptime("2021-06-15", "%Y-%m-%d"), book2.publication_date)
        library.catalog.add_book_item(book_item1)
        library.catalog.add_book_item(book_item2)

        # Users
        card_member = LibraryCard("CARD1001", datetime.now())
        person_member = Person("Alice", lib_address, "alice@email.com", "345678")
        member = Member("MEM001", "pass", person_member, card_member)

        card_librarian = LibraryCard("CARD2001", datetime.now())
        person_librarian = Person("Libby", lib_address, "libby@email.com", "456789")
        librarian = Librarian("LIB001", "pass", person_librarian, card_librarian)

        # SCENARIO 1: Search and Reserve
        print("\n------------------------------")
        print(">>> SCENARIO 1: Member searches and reserves a book")
        print("------------------------------\n")

        found_books = library.catalog.search_by_title("Pride and Prejudice")
        if found_books:
            book_item = found_books[0]
            print(f"-> Member [{member.person.name}] attempts to reserve book item [{book_item.id}]")
            member.reserve_book_item(book_item)
            print(f"-> Member [{member.person.name}] checks out reserved book item [{book_item.id}]")
            member.checkout_book_item(book_item)
        else:
            print("Book not found.")

        # SCENARIO 2: Return Book (Late Return)
        print("\n------------------------------")
        print(">>> SCENARIO 2: Member returns the book late")
        print("------------------------------\n")
        book_item1.due_date = datetime.now() - timedelta(days=3)
        print(f"-> Member [{member.person.name}] returns book item [{book_item1.id}] after due date.")
        member.return_book_item(book_item1)

        # SCENARIO 3: Renew Book
        print("\n------------------------------")
        print(">>> SCENARIO 3: Member renews a book")
        print("------------------------------\n")
        print(f"-> Member [{member.person.name}] checks out the book again.")
        member.checkout_book_item(book_item1)
        print(f"-> Member [{member.person.name}] renews the book.")
        member.renew_book_item(book_item1)

        # NOTIFICATIONS
        print("\n------------------------------")
        print(">>> NOTIFICATIONS")
        print("------------------------------\n")
        email_notification = EmailNotification("N001", "Your book is overdue!", member.person.email)
        email_notification.send_notification()

        postal_notification = PostalNotification("N002", "Please return your book!", member.person.address)
        postal_notification.send_notification()

        print("\n========== END OF DEMO ==========\n")

    except Exception as ex:
        print("Exception occurred:", ex)
