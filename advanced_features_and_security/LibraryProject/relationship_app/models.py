"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [("can_add_book", "Can add books"), ("can_change_book", "Can change book"), ("can_delete_book", "Can delete book")]

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'

    ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (LIBRARIAN, 'librarian'),
        (MEMBER, 'member')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=MEMBER)
"""

from django.db import models
from django.conf import settings  # <-- use this for the custom user model

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add books"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book")
        ]


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


class UserProfile(models.Model):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'

    ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (LIBRARIAN, 'librarian'),
        (MEMBER, 'member')
    ]

    # ✅ Use the custom user model here
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=MEMBER)

    def __str__(self):
        return str(self.user)


