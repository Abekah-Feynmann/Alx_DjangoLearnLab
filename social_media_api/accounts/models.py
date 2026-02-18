from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#Creating a custom user model with fields for bio, profile_picture and followers
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True)
    followers = models.ManyToManyField(CustomUser, related_name='followers', symmetrical=False )

