import pandas as pd

class BookLover():
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        if type(name) != str:
            raise TypeError('name must be a string')
        if type(email) != str:
            raise TypeError('email must be a string')
        if type(fav_genre) != str:
            raise TypeError('fav_genre must be a string')
        if type(num_books) != int:
            raise TypeError('num_books must be an integer')
        if type(book_list) != pd.DataFrame:
            raise TypeError('book_list must be a pandas DataFrame')
        if num_books != len(book_list):
            raise ValueError('num_books must = number of books in book_list')
        
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, book_rating):
        if type(book_name) != str:
            raise TypeError('book_name must be a string')
        if type(book_rating) != int:
            raise TypeError('book_rating must be an integer')
        if book_rating < 0 or book_rating > 5:
            raise ValueError('book_rating must be between 1 and 5')
        
        if book_name not in self.book_list['book_name'].to_list():
            new_book = pd.DataFrame({'book_name':[book_name], 'book_rating':[book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1

    def has_read(self, book_name):
        if type(book_name) != str:
            raise TypeError('book_name must be a string')
        
        books_read = self.book_list['book_name'].to_list()
        return book_name in books_read
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    book_lover = BookLover('Colby', 'ncc9kn@virginia.edu', 'Mystery')
    book_lover.add_book('test', 5)
    print(book_lover.has_read('test'))
    print(book_lover.has_read('not test'))
    print(book_lover.num_books_read())
    print(book_lover.fav_books())