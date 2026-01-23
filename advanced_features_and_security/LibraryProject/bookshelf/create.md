#create.md
    >>> from bookshelf.models import Book
    >>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1984)
    >>> book.save()
    #expected output
    >>>
 