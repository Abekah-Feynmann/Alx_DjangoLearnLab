from .models import Book

#List of all books in the library
library_name = "Abekah's Library"
library = Library.objects.get(name=library_name)
all_books = Library.books.all()