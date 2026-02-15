from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin



    
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
    Implementing CRUD operations
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
    template_name = 'post_create.html'
    context_object_name = 'post_create'

#Enable post authors to edit their posts
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_update.html'
    context_object_name = 'post_update'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


#Let authors delete their post
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'post_delete.html'
    context_object_name = 'post_delete'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author






