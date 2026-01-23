#retrieve.md
    >>> books = Book.objects.get()
    for book in Book.objects.get():
         print(book.title, book.author, book.publication_year)

    #expected output
    1984 George Orwell 1984
