class Book:
    """
    A class representing a book in the library.
    """
    def __init__(self, title, author):
        """
        Initializes the Book instance with a title, author, and a private attribute to track availability.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out if it is available.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as returned (available) if it was checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is available for checkout.
        """
        return not self._is_checked_out


class Library:
    """
    A class representing a library that manages a collection of books.
    """
    def __init__(self):
        """
        Initializes the Library instance with a private list of books.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a new book to the library's collection.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title if it is available in the library.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out: {title}")
                    return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Returns a book by title if it is checked out.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned: {title}")
                    return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """
        Lists all books in the library that are currently available for checkout.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
