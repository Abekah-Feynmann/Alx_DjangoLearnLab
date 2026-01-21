from django.urls import path, include
from .views import LibraryDetailView
from .views import list_books, admin_view, member_view, librarian_view, add_book, delete_book, change_book


urlpatterns = [
    path('relationship_app/', list_books, name='list_books'), 
    path('relationship_app/', LibraryDetailView.as_view()),
    path('relationship_app/', include('django.contrib.auth.urls')), 
    path('relationship_app/login', LoginView.as_view(template_name='relationship_app/login.html', name='login')),
    path('relationship_app/logout', LogoutView.as_view(template_name='relationship_app/logout.html', name='logout')),
    path('relationship_app/register',views.register, name='register'),
    path('relationship_app/', admin_view), 
    path('relationship_app/', member_view),
    path('relationship_app/', librarian_view),
    path('relationship_app/edit_book/', change_book),
    path('relationship_app/add_book/', add_book),
    path('relationship_app/delete_book', delete_book),
]