from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnFollowUserView
from rest_framework.authtoken import views

urlpatterns = [
    #A route to the ProfileView
    path("profile/", ProfileView.as_view(), name="profile"),

    #A route to the LoginView
    path("login/", LoginView.as_view(), name="login"),

    #Aroute to the RegisterView
    path("register/", RegisterView.as_view(), name="register"),

    #A mechanism for users to obtain a token given their username and password
    path("api-token-auth/", views.obtain_auth_token),

    #A route for follow management
    path("follow/<int:user_id>", FollowUserView.as_view(), name="follow"),
    path("unfollow/<int:user_id>", UnFollowUserView.as_view(), name="unfollow"),
]