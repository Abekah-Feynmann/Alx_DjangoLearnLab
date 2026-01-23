from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

#Setting up a custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    def __str__(self):
        return self.username

#create a Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        email = self.normalize_email()
        return User

    def create_superuser(self, email, password=None):
        extra_fields.setdefault('self.Admin', True)
        extra_fields.setdefault('self.superuser', True)

        if extra_fields.get("self.superuser") is not True:
            raise ValueError("SuperUser must have is_superuser=True")
        elif extra_fields.get("self.Admin") is not True:
            raise ValueError("Super User mus thave is_staff=True")
        return self.create_user(email, password)
