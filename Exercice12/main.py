class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.borrowed_books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Le livre '{book.title}' a été ajouté à la bibliothèque.")

    def remove_book(self, book_title: str):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Le livre '{book_title}' a été supprimé de la bibliothèque.")
                return
        print(f"Le livre '{book_title}' n'a pas été trouvé dans la bibliothèque.")

    def borrow_book(self, book_title: str):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                print(f"Le livre '{book_title}' a été emprunté.")
                return
        print(f"Le livre '{book_title}' n'est pas disponible pour emprunt.")

    def return_book(self, book_title: str):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"Le livre '{book_title}' a été retourné à la bibliothèque.")
                return
        print(f"Le livre '{book_title}' n'a pas été trouvé parmi les livres empruntés.")

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        return [book.title for book in self.borrowed_books]


# Example usage:
library = Library()

book1 = Book("TEST", "TEST", 1950)
book2 = Book("TEST1", "TEST1", 2000)
book3 = Book("TEST2", "TEST2", 2020)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Livres disponibles :", library.available_books())
library.borrow_book("TEST")
print("Livres empruntés :", library.borrowed_books_list())
library.return_book("TEST")
print("Livres disponibles après retour :", library.available_books())
