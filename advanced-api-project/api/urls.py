from .models import Book
from django.urls import path
from .views import ListView, DetailView, DeleteView, UpdateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('books', ListView, basename=None)


#Connecting views with specific endpoints

urlpatterns = [
    path('/books/', ListView.as_view(), name='book-list'),
    path('books/retrieve', DetailView.as_view(), name='book-detail'),
    path('books/delete', DeleteView.as_view(), name='book-delete'),
    path('books/delete', CreateView.as_view(), name='book-create'),
]