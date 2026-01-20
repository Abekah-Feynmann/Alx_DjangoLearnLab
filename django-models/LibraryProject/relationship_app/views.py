from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create a function-based view that list all books in the database.
def list_books(request):
    books = Book.objects.all()
    context = {"book_list":books}
    return render(request, 'relationship_app/list_books.html', context)

#Create a class-based view that list all books in a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()
        
        return render(request, 'templates/relationship_app/register.html')

# create an admin view that only those with admin password can access
def is_admin(user):
    return(
        user.is_authenticated and
        user.userprofile.role == 'Admin'
    ) 

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'templates/relationship_app/admin_view.html')


#the role checking function
def is_member(user):
    return(
        user.is_authenticated and
        user.userprofile.role == 'Member'
    )

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'templates/relationship_app/member_view.html')


    




