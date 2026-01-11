
#create.md
    >>> from bookshelf.models import Book
    >>> book = Book(title="1984", author="George Orwell", publication_year=1984)
    >>> book.save()
    #expected output
    >>>

#retrieve.md
    >>> books = Book.objects.all()
    for book in Book.objects.all():
         print(book.title, book.author, book.publication_year)

    #expected output
    1984 George Orwell 1984

#update.md
    >>> book = Book.objects.get()
    >>> book.title = "Nineteen Eighty-Four"
    >>> book.save()

    #expected output
    >>> 

#delete.md
>>> book = Book.objects.get()
>>> book.delete()

#expected output
(1, {'bookshelf.Book': 1})