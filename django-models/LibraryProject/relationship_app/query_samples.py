from .models import Book

#Get all books written by a certain author
books = Book.objects.all()
