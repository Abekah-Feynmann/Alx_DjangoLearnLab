#retrieve.md
    >>> books = Book.objects.all()
    for book in Book.objects.all():
         print(book.title, book.author, book.publication_year)

    #expected output
    1984 George Orwell 1984
