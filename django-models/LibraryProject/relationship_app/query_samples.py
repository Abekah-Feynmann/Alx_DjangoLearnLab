from .models import Book

#List of all books in the library
library = Library.objects.get(name="Abekah's Library")
all_books = Library.books.all()