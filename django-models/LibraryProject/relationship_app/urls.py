from django.urls import path, include
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('relationship_app/', list_books), 
    path('relationship_app/', LibraryDetailView.as_view()),
    path('relationship_app/', include('django.contrib.auth.urls'))
]