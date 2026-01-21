from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required


# Create a function-based view that lists all books in the database.
def list_books(request):
    books = Book.objects.all()
    context = {"book_list":books}
    return render(request, 'relationship_app/list_books.html', context)

#Create a class-based view that lists all books in a library
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

#create a member_view that only those with member password can access
#the role checking function
def is_member(user):
    return(
        user.is_authenticated and
        user.userprofile.role == 'Member'
    )

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'templates/relationship_app/member_view.html')


#create a librarian view that only those with librarian password can access
#role checking function

def is_librarian(user):
    return(
        user.is_authenticated and
        user.userprofile.role == 'Librarian'
    )

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'templates/relationship_app/librarian_view.html')

    
#create a view that adds book under permissions
@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]

        Book.objects.create(
            title = title,
            author = author
        )

        return redirect('list_books')
    return render(request, 'templates/relationship_app/add_book.html')


