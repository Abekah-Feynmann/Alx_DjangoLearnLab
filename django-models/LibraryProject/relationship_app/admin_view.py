from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# create an admin view that only those with admin password can access
def is_admin(user):
    return(
        user.is_authenticated and
        user.userprofile.role == 'Admin'
    ) 

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')