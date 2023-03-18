class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        if title not in self.books:
            self.books.append(title)

    def find_book(self, title):
        if title in self.books:
            return title


