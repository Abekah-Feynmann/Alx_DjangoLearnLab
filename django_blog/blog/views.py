from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .models import Post, Comment



    
# Creating the signup view (User Registration)
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#A view that allows authenticated users to edit their profile
@login_required
def ProfileView(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "blog/profile.html", {"form":form})


"""
    Implementing CRUD operations for Post Model
"""
#Creating the List view to display blog posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    paginate_by = 10

#Creating the DetailView to show individual blog posts
class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'

#Allow authenticated users to create new posts
class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    permission_required = 'blog.add_post'
    template_name = 'post_form.html'
    context_object_name = 'post_create'

#Enable post authors to edit their posts
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    context_object_name = 'post_update'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


#Let authors delete their post
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post_confirm_delete'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


"""
Implementing the CRUD operations for Comment Model
"""

#A view to display comments under a blog post
class CommentListView(ListView):
    model = Comment
    template_name = "comment_list.html"
    context_object_name = "comment_list"
    paginate_by = 10

#A view for login users to comment under posts
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "comment_form.html"
    context_object_name = "comment_form"


#A view for updating comments
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = "comment_form.html"
    context_object_name = "comment_form"
    fields = ["content"]
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

#A view for deleting comments
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('comment-list')
    template_name = "comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author





