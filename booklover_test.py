import unittest
from booklover.booklover import BookLover
import pandas as pd

class TestBookLover(unittest.TestCase):
    def test_1_add_book(self):
        book_lover = BookLover('Colby', 'ncc9kn@virginia.edu', 'Test')
        book_lover.add_book('test', 5)

        actual = [tuple(book) for book in book_lover.book_list.to_records(index = False)]
        expected = [('test', 5)]
        self.assertEqual(actual, expected)

    def test_2_add_book(self):
        book_lover = BookLover('Colby', 'ncc9kn@virginia.edu', 'Test')
        book_lover.add_book('test', 5)
        book_lover.add_book('test', 5)

        actual = [tuple(book) for book in book_lover.book_list.to_records(index = False)]
        expected = [('test', 5)]
        self.assertEqual(actual, expected)

    def test_3_has_read(self):
        book_lover = BookLover('Colby', 'ncc9kn@virginia.edu', 'Test')
        book_lover.add_book('test', 5)

        actual = book_lover.has_read('test')
        self.assertTrue(actual)

    def test_4_has_read(self):
        book_lover = BookLover('Colby', 'ncc9kn@virginia.edu', 'Test')
        book_lover.add_book('test', 5)

        actual = book_lover.has_read('not test')
        self.assertFalse(actual)

    def test_5_num_books_read(self):
        book_lover = BookLover('Colby', 'ncc9kn@virginia.edu', 'Test')
        book_lover.add_book('test 1', 5)
        book_lover.add_book('test 2', 4)
        book_lover.add_book('test 3', 3)
        book_lover.add_book('test 4', 2)
        book_lover.add_book('test 5', 1)

        actual = book_lover.num_books_read()
        expected = 5
        self.assertEqual(actual, expected)

    def test_6_fav_books(self):
        book_lover = BookLover('Colby', 'ncc9kn@virginia.edu', 'Test')
        book_lover.add_book('test 1', 5)
        book_lover.add_book('test 2', 4)
        book_lover.add_book('test 3', 3)
        book_lover.add_book('test 4', 2)
        book_lover.add_book('test 5', 1)

        actual = [tuple(book) for book in book_lover.fav_books().to_records(index = False)]
        expected = [('test 1', 5), ('test 2', 4)]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity = 3)