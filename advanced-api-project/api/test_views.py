from .models.py import Book
from rest_framework.test import APITestCase
from rest_framework import status
from .views import CreateView, UpdateView, DeleteView



class BookTestCase(APITestCase):
    data = {
            "author": 'Peggy Oppong',
            "title": "End of the tunnel"
            }
    def test_create(self):
        response = self.client.post(f"/api/books/", data, format='json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["author"], "Peggy Oppong")
        self.assertEqual(response.data["title"], "End of the tunnel")
        self.assertEqual(Book.objects.count(), 1)

    def test_update(self):
        update_payload = {
            "author":"Dostoevsky",
            "title":"Crime and Punishment"
        }

        #create a new object
        update_data = Book.objects.create(
            author="Dostoevsky",
            title="The Brothers Karamazov"
        )

        response = self.client.put(f"/api/books/{update_data.id}/", update_payload, format="json")

        #Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Crime and Punishment")

        #Confirm database updated
        update_data.refresh_from_db()
        self.assertEqual(update_data.title, "Crime and Punishment")


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
        