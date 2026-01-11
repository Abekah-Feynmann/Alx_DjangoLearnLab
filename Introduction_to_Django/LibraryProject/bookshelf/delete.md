#delete.md
>>> book = Book.objects.get()
>>> book.delete()

#expected output
(1, {'bookshelf.Book': 1})