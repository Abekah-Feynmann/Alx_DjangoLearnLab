from django.db import models

# Create your models here.

#A book model with title and author
class Book(models.Model):
    title = model.CharField(max_length=200)
    author = model.CharField(max_length=100)
    
    

