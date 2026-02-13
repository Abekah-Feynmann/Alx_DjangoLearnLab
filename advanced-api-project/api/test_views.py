from .models.py import Book
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from .views import CreateView


factory = APIRequestFactory()

class BookTestCase(APITestCase):
    def test_create(self):
        request = factory.post('api/books/', {
            author: 'Peggy Oppong',
            title: "End of the tunnel"

        }, format= 'json')
        view = CreateView.as_view()
        response = view(request)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)

    def test_update(self):
        author_name = Book.objects.get(author= "Peggy Oppong", title="End of the tunnel")
        response = self.client.get('books/update')
        self.assertEqual(response_code, 200)

    def test_delete(self):
        