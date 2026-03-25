from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from notifications.models import Notification


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
                user=post.author,
                message=f"{request.user} liked your post"
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

#Creating a View that generates a feed based on the posts from users that the current user follows
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # get current user
    def get_queryset(self):
        user = self.request.user()

        #get users followed by the current user
        following_users = user.following.all()

        #get all posts from those users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('created_at')


#A view that handles liking and unliking posts.
class LikeView(generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer 

    def post(self, request):
        #extract the data and validate it
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #get the post instance and the user instance
        post = serializer.validated_data["post"]
        user = request.user

        if Like.objects.filter(user=user, post=post).exists():
            return Response({"error":"Already Liked"}, status=400)
        serializer.save(user=user)
        return Response(serializer.data, status=201)

