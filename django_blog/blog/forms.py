from django.contrib.auth.forms import UserCreationForm
from django import forms
from taggit.forms import TagWidget

#Create a custom UserCreationForm to include email
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.textarea, required=False)

    class Meta:
        model = User
        fields = ["username","email"]

#Create a ProfileUpdateForm
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["Username", "Password", "Email"]

#Create a comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment ...'})
        }

#The PostForm
class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget)

    class Meta:
        model = Post
        fields = ["title", "tags"]
        

