from .models import Book
from django.urls import path
from .views import ListView, DetailView, DeleteView, UpdateView, CreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('books', ListView, basename=None)


#Connecting views with specific endpoints

urlpatterns = [
    path('/books/', ListView.as_view(), name='book-list'),
    path('books/retrieve', DetailView.as_view(), name='book-detail'),
    path('books/delete', DeleteView.as_view(), name='book-delete'),
    path('books/create', CreateView.as_view(), name='book-create'),
    path('books/update', UpdateView.as_view(), name='book-update'),
]