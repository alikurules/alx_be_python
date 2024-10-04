class Book:
    def __init__(self, title, author):
        
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"Book '{self.title}' has been checked out.")
        else:
            print(f"Book '{self.title}' is already checked out.")

    def return_book(self):
        
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' was not checked out.")

    def is_available(self):
        
        return not self._is_checked_out


class Library:
    def __init__(self):
        
        self._books = []

    def add_book(self, book):
        
        self._books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def check_out_book(self, title):
        
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                else:
                    print(f"Book '{title}' is currently not available.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                else:
                    print(f"Book '{title}' was not checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
            return
        for book in available_books:
            print(f"{book.title} by {book.author}")
