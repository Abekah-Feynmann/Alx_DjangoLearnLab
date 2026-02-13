from .models.py import Book
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from .views import CreateView, UpdateView, DeleteView


factory = APIRequestFactory()

class BookTestCase(APITestCase):
    def test_create(self):
        request = factory.post('api/books/', {
            author: 'Peggy Oppong',
            title: "End of the tunnel"

        }, format='json')
        view = CreateView.as_view()
        response = view(request)
        
        self.assertEqual(response.status_code, 201),
        self.assertEqual(response.data["author"], "Peggy Oppong"),
        self.assertEqual(response.data["title", "End of the tunnel"])
        self.assertEqual(Book.objects.count(), 1)

    def test_update(self):
        #Create an object
        book = Book.objects.create(
            author="Dostoevsky",
            title = "Crime and Punishment"
        )

        #create a new object
        data = Book.objects.create(
            author="Dostoevsky",
            title="The Brothers Karamazov"
        )

        request = factory.put(f"/api/books/{book.id}/", data, format="json")
        view = UpdateView().as_view
        response = view(request, pk=book.id)

        #Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "The Brothers Karamazov")

        #Confirm database updated
        book.refresh_from_db()
        self.assertEqual(book.title, "The Brothers Karamazov")


    def test_delete(self):
        #create a new instance of book
        book = Book.objects.create(
            author="Dostoevsky",
            title="Notes from Underground"
        )

        request = factory.delete(f"/api/books/{book.id}/")
        view = DeleteView.as_view()
        response = view(request, pk=book.id)

        #Assertions
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Book.objects.count(), 0)
        