from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}  # { author: [book_1, book_2 ...], author_2: ...}
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:

        if author in self.books_available:
            if book_name in list(self.books_available[author]):
                self.books_available[author].remove(book_name)
                if user.username in self.rented_books:
                    self.rented_books[user.username][book_name] = days_to_return
                else:
                    self.rented_books[user.username] = {book_name: days_to_return}

                user.books.append(book_name)

                return f"{book_name} successfully rented for the next {days_to_return} days!"

        days_left = self.rented_books[user.username][book_name]
        return f"The book \"{book_name}\" is already rented and will be available in {days_left} days!"

    def return_book(self, author:str, book_name:str, user: User) -> str or None:

        if book_name in user.books:

            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)
            user.books.remove(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"
