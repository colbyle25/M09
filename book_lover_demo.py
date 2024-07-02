from booklover import booklover

if __name__ == '__main__':
    book_lover = booklover.BookLover('Colby', 'ncc9kn@virginia.edu', 'Mystery')
    book_lover.add_book('test', 5)
    print(book_lover.num_books_read())