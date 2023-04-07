from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(3)

    def test_init(self):
        self.assertEqual(3, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_setter_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

        with self.assertRaises(ValueError) as ve2:
            self.bookstore.books_limit = -2
        self.assertEqual("Books limit of -2 is not valid", str(ve2.exception))

    # receive_book method test

    def test_receive_book_update_availability(self):
        self.bookstore.receive_book("book_1", 2)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles["book_1"])

    def test_receive_book_output(self):
        actual = self.bookstore.receive_book("book_1", 2)
        expected = "2 copies of book_1 are available in the bookstore."
        actual2 = self.bookstore.receive_book("book_2", 1)
        self.assertEqual(expected, actual)
        self.assertEqual({'book_1': 2, 'book_2': 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["book_2"])
        self.assertEqual("1 copies of book_2 are available in the bookstore.", actual2)

    def test_receive_same_book(self):
        self.bookstore.receive_book("book_1", 2)
        result = self.bookstore.receive_book("book_1", 1)
        self.assertEqual({"book_1": 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("3 copies of book_1 are available in the bookstore.", result)

    def test_receive_book_limit_reached(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("book_1", 5)
        self.assertEqual(3, self.bookstore.books_limit)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    # __len__ test

    def test_len_override(self):
        self.bookstore.receive_book("book_1", 2)
        self.assertEqual(2, len(self.bookstore))

    # sell_book method test

    def test_sell_book_not_in_bookstore_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book2", 1)
        self.assertEqual("Book book2 doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_copies_exception(self):
        self.bookstore.receive_book("book_1", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book_1", 3)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles["book_1"])
        self.assertEqual("book_1 has not enough copies to sell. Left: 2", str(ex.exception))

    def test_sell_book_update_availability(self):
        self.bookstore.receive_book("book_1", 2)
        self.bookstore.sell_book("book_1", 1)
        self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["book_1"])

    def test_sell_book_total_sold_books(self):
        self.bookstore.receive_book("book_1", 2)
        self.bookstore.sell_book("book_1", 1)
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles["book_1"])

    def test_sell_book_final_return(self):
        self.bookstore.receive_book("book_1", 2)
        result = self.bookstore.sell_book("book_1", 1)
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual("Sold 1 copies of book_1", result)

    def test_str_output(self):
        self.bookstore.receive_book("book_1", 2)
        self.bookstore.sell_book("book_1", 1)
        self.bookstore.receive_book("book_2", 1)

        expected = f"Total sold books: 1\n"\
                   f'Current availability: 2\n'\
                   f" - book_1: 1 copies\n" \
                   f" - book_2: 1 copies"

        self.assertEqual(expected, self.bookstore.__str__())


if __name__ == "__main__":
    main()

