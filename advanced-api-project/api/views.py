from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied


#A set of generic views for the Book model to handle CRUD operations

# A listview for retrieving all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#A detailview for retrieving a single Book by ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#Create view for adding a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        """
        Runs after validation passes
        """
        if not self.request.user.is_staff:
            raise PermissionDenied("Only staff users can create books")
        serializer.save(owner=self.request.user)

#Update view for modifying an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        FILTER who can update what
        """
        user = self.request.user

        if user.is_staff:
            return Book.objects.all()
        
        #Non-staff users can only update their own books
        return Book.objects.filter(owner=user)

    def perform_update(self, serializer):
        """
        Extra logic before saving updates
        """
        if serializer.instance.owner != self.request.user:
            raise PermissionDenied("You do not own this book")
        serializer.save()


#Delete view for removing a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [Isauthenticated]
