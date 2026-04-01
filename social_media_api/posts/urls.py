from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

"""
    Using the default router because we are working with viewsets.
"""
router = DefaultRouter()

#register each view
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),

    #paths for liking and unliking posts
    path("post/<int:pk>/like/", PostViewSet.as_view({"post": "like"}), name="like"),
    path("post/<int:pk>/unlike/", PostViewSet.as_view({"post": "unlike"}), name="unlike"),
]