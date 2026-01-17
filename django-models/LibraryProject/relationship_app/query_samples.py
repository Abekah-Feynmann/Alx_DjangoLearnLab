from .models import Book

#List of all books in the library
library_name = "Abekah's Library"
library = Library.objects.get(name=library_name)
all_lib_books = Library.books.all()

#Query all books by a specific author
author_name = "Peggy Oppong"
author = Author.objects.get(name=author_name)
all_auth_books = Book.objects.filter(author=author)

#Retrieve the Librarian for a Library
librarian = Librarian.objects.get(library=library)

