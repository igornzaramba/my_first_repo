class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            print(f"Book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"Book '{self.title}' is already checked out.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' is already available.")

class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the catalogue.")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f"'{book.title}' by {book.author}")

def main():
    library = LibraryCatalogue()

    # Add sample books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    library.add_book(book2)

    # Check out and return books
    book1.check_out()
    book1.return_book()
    book2.check_out()

    # Display available books
    library.display_books()


main()
