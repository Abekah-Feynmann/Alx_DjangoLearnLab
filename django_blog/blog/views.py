from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

#Create a custom UserCreationForm to include email
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    class Meta:
        model = User
        fields = ("Username", "Password", "Email")

    
# Creating the signup view (User Registration)
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#Creating the login view
class LoginView(views.LoginView):


