from Search import Search
from collections import defaultdict
from datetime import datetime

class Catalog(Search):
    def __init__(self):
        self.book_titles = defaultdict(list)
        self.book_authors = defaultdict(list)
        self.book_subjects = defaultdict(list)
        self.book_publication_dates = defaultdict(list)
        self.all_book_items = {}

    def add_book_item(self, book_item):
        self.all_book_items[book_item.id] = book_item

        # By title
        self.book_titles[book_item.book.title].append(book_item)

        # By author
        for author in book_item.book.authors:
            self.book_authors[author.name].append(book_item)

        # By subject
        self.book_subjects[book_item.book.subject].append(book_item)

        # By publication date
        pub_date_str = book_item.book.publication_date.strftime('%Y-%m-%d')
        self.book_publication_dates[pub_date_str].append(book_item)

    def search_by_title(self, title):
        return self.book_titles.get(title, [])

    def search_by_author(self, author):
        return self.book_authors.get(author, [])

    def search_by_subject(self, subject):
        return self.book_subjects.get(subject, [])

    def search_by_publication_date(self, pub_date):
        date_str = pub_date.strftime('%Y-%m-%d')
        return self.book_publication_dates.get(date_str, [])
