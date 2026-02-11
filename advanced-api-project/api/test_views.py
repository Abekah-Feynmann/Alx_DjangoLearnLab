from django.test import TestCase
from .models.py import Book

class BookTestCase(tests.unittest):
    def test_create(self):
        Book.objects.create(author='Peggy Oppong', title="End of the tunnel" )
        self.assertEqual(book.title, "End of the tunnel")

    def test_update(self):
        author_name = Book.objects.get(author= "Peggy Oppong", title="End of the tunnel")