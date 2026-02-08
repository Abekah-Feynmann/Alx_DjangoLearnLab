from .models import Book
from django.urls import path
from .views import ListView, DetailView, DeleteView, UpdateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('books', ListView, basename=None)


#Connecting views with specific endpoints

urlpatterns = [
    path('/books/', ListView.as_view(), name='book-list')
]