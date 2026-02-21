from rest_framework import serializers
from .models import Post, Comment


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

