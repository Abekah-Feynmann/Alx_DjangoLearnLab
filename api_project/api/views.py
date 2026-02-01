from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics


# Create your views here.

#Defines a view that uses BookSerializer to return and retrieve book data
class BookList(generics.ListAPIView):
    queryset = Book
    serializer_class = BookSerializer


