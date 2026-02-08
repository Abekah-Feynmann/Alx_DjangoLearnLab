from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


#A set of generic views for the Book model to handle CRUD operations

# A listview for retrieving all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#A detailview for retrieving a single Book by ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Create view for adding a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Update view for modifying an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Delete view for removing a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
