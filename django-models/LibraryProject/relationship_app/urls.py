from django.urls import path, include
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('relationship_app/', list_books), 
    path('relationship_app/', LibraryDetailView.as_view()),
    path('relationship_app/', include('django.contrib.auth.urls')), 
    path('relationship_app/login', LoginView.as_view(template_name='relationship_app/login.html', name='login')),
    path('relationship_app/logout', LogoutView.as_view(template_name='relationship_app/logout.html', name='logout')),
    path('relationship_app/register',views.register, name='register'),
]