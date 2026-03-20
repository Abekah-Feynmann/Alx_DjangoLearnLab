from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
#Creating a custom user model with fields for bio, profile_picture and followers
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    following = models.ManyToManyField("self", symmetrical=False, related_name = "followers", blank=True)

    def __str__(self):
        return self.username



