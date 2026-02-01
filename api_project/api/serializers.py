from .models import Book
from rest_framework import serializers

#A book serializer class that includes all fields of the book model
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']
