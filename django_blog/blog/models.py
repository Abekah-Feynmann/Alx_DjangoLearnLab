from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.


#The Post Model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Posts")

#The Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

#The Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name='tags')
    tag = TaggableManager()


