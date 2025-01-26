class Book:
    """
    A base class representing a generic book.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance with title and author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book instance.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    A class representing an electronic book (EBook), inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance with title, author, and file size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook instance.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A class representing a printed book (PrintBook), inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance with title, author, and page count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook instance.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class representing a library that manages a collection of books.
    """
    def __init__(self):
        """
        Initializes the Library instance with an empty collection of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook) to the library's collection.
        """
        self.books.append(book)

    def list_books(self):
        """
        Lists all books in the library with their details.
        """
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
