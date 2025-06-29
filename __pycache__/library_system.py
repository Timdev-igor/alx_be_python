class Book :
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
     return f"'{self.title}' by {self.author}"

class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author,)
        self.file_size=file_size

    def __str__(self):
     return f"'{self.title}' by {self.author} (E-Book, {self.file_size}MB)"

class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author)
        self.page_count=page_count

    def __str__(self):
     return f"'{self.title}' by {self.author} (Print Book, {self.page_count} pages)"

class Library:
    def __init__(self):
        self.books = []  # A list to store books of various types

    def add_book(self, book):
        self.books.append(book)  # Adds any instance of Book (or its subclasses)

    def list_books(self):
        for book in self.books:
            print(book)  # Calls the __str__ method of each book