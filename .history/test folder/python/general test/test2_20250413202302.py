class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library(Book):
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        return [str(book) for book in self.books]

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    