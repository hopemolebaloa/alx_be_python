class Book:
    """
    A class representing a book with attributes for title, author, and publication year.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the book instance.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
