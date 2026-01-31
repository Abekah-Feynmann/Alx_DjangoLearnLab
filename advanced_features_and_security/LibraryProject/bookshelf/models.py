from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_view', "Can view Book"),
            ("can_edit", "can make changes to Book"),
            ("can_delete", "can make deletions"),
            ("can_create", "can create new book"),
        ]

    def __str__(self):
        return self.title

#create a Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The username must be set")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email, 
            **extra_fields
            )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('self.superuser', True)

        if extra_fields.get("self.superuser") is not True:
            raise ValueError("SuperUser must have is_superuser=True")
        elif extra_fields.get("self.is_staff") is not True:
            raise ValueError("SuperUser must have is_staff=True")
        return self.create_user(username, email, password, **extra_fields)


#Setting up a custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to= 'profiles/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


"""
#Integrate the Custom User Model into Admin
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "password"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields":["email", "password"]}),
        ("Permissions", {"fields": ["is_Admin"]}),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

#Defining Custom Permissions for a model

#get permission
permission = Permission.objects.filter(
    codename__in=['can_view', 'can_edit', 'can_create', 'can_delete'])
CustomUser.user_permissions.add(permission)
"""
