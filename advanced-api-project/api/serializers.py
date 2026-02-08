from .models import Book, Author
from rest_framework import serializers
import datetime

#A book serializer class that serializes all fields in the book model
#It validates the publication year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        current_year = datetime.datetime.now().year

        if data['publication_year'] > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return data


#An Author serializer which serializes the name field in Author model
#Author.books returns multiple objects
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']