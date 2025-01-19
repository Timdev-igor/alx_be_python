class Book:
    """Represents a book with a title, an author, and its availability status."""

    def __init__(self, title, author):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library's collection.

        Args:
            book (Book): The book to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.

        Args:
            title (str): The title of the book to check out.

        Returns:
            str: Success or error message.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out."
                return f"'{title}' is already checked out."
        return f"Book '{title}' not found in the library."

    def return_book(self, title):
        """
        Return a book by its title.

        Args:
            title (str): The title of the book to return.

        Returns:
            str: Success or error message.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' has been returned."
                return f"'{title}' was not checked out."
        return f"Book '{title}' not found in the library."

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
