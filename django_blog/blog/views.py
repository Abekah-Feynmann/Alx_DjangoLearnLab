from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required


    
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




