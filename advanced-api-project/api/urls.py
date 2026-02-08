from .models import Book
from django.urls import path
from .views import ListView, DetailView, DeleteView, UpdateView, CreateView



#Connecting views with specific endpoints

urlpatterns = [
    path('/books/', ListView.as_view(), name='book-list'),
    path('books/retrieve/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
    path('books/create', CreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
]