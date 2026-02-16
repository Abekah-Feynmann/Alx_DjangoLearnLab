from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from blog.views import (PostListView, 
                        PostDetailView, 
                        PostCreateView, 
                        PostUpdateView, 
                        SignUpView,
                        CommentCreateView,
                        CommentListView, 
                        CommentUpdateView,
                        CommentDeleteView
)


urlpatterns = [
    path('profile/', TemplateView.as_view(template_name='blog/profile.html'), name='profile'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #Blog-Post Urls

    #For the PostViews
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    #For the CommentViews
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
