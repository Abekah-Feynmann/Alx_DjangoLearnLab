from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


# Setting up CRUD operations for both Post and Comments.
"""
Using the ModelviewSet gives one access to all the CRUD operations needed. 
the viewset class would be more fitting if the operations needed are customized.
"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ["IsAuthenticated"]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = ["IsAuthenticated"]


