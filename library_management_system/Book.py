from BookFormat import BookFormat

class Book:
    def __init__(self, isbn, title, subject, publisher, publication_date,
                 language, number_of_pages, book_format: BookFormat, authors):
        self.isbn = isbn
        self.title = title
        self.subject = subject
        self.publisher = publisher
        self.publication_date = publication_date
        self.language = language
        self.number_of_pages = number_of_pages
        self.format = book_format
        self.authors = authors  # List of Author objects
