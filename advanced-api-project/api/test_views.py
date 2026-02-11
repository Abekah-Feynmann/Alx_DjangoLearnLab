from .models.py import Book
from rest_framework.tests import APITestCase
from rest_framework import status

class BookTestCase(APITestCase):
    def test_create(self):
        Book.objects.create(author='Peggy Oppong', title="End of the tunnel" )
        response = self.client.get('api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update(self):
        author_name = Book.objects.get(author= "Peggy Oppong", title="End of the tunnel")
        self.assertEqual()