from rest_framework import serializers
from .models import Post, Comment, Like


#Creating the serializer for Post
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
        
    class Meta:
        model = Post
        fields = "__all__"

# A serilizer for the Comment Model
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

#A serializer for the Like Model
"""
 This part is not necessary as like is a behaviour and not a resource.
 However, the LikeSerializer is being kept in case there might be the need for a change.
"""
class LikeSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = "__all__"
