from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('relationship_app/', list_books), 
    path('relationship_app/', LibraryDetailView.as_view()),
]