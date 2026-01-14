from .models import Book

books = Book.objects.all()
for book in books:
    print(book)