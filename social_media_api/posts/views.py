from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


# Setting up CRUD operations for both Post and Comments.
"""
Using the ModelviewSet gives one access to all the CRUD operations needed. 
the viewset class would be more fitting if the operations needed are customized.
"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    #liking a post
    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor = request.user,
                verb=f"{request.user} liked your post",
                content_type = ContentType.objects.get_for_model(post),
                object_id = post.id 
                timestamp = timezone.now()
            )
            return Response({"status":"liked"}, status = status.HTTP_201_CREATED)
        return Response({"status":"already liked"}, status = status.HTTP_200_OK)

    #unliking a post
    @action(detal=True, methods=[post])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()            
            return Response({"status": "unliked"}, status=status.HTTP_200_OK)
        return Response({"status": "not liked"}, status=status.HTTP_400_BAD_REQUEST)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        comment = serializer.save(author = self.request.user)
        post = comment.post
        if self.request.user != post.author:
            Notification.objects.create(
                recipient = post.author,
                actor = self.request.user,
                verb = f"{request.user} commented on your post",
                content_type = ContentType.objects.get_for_model(post),
                object_id = post.id,
                timestamp = timezone.now()
            )

#Creating a View that generates a feed based on the posts from users that the current user follows
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # get current user
    def get_queryset(self):
        user = self.request.user()
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('created_at')



