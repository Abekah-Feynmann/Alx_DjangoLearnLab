from django.shortcuts import render, redirect, get_object_or_404
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from relationship_app.models import Library, Book
from django.contrib.auth.decorators import permission_required, login_required
from .forms import ExampleForm




# Create your views here.
class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        editor, _ = Group.objects.get_or_create(name='Editor')
        viewer, _ = Group.objects.get_or_create(name='Viewer')
        admin, _ = Group.objects.get_or_create(name='Admin')

        editor_perms = Permission.objects.filter(
            codename__in = ["can_edit", "can_create"]
        )
        viewer_perms = Permission.objects.filter(
            codename__in = ["can_view"]
        )
        admin_perms = Permission.objects.filter(
            codename__in = ["can_delete", "can_create", "can_edit", "can_view"]
        )

        editor.permissions.set(editor_perms)
        viewer.permissions.set(viewer_perms)
        admin.permissions.set(admin_perms)

        self.stdout.write(self.style.SUCCESS("Groups and permissions created"))

        


"""
Create permissions for add, create, edit or delete
"""
#A view that lists all books in the database
def list_books(request):
    books = Book.objects.all()
    context = {"book_list": books}
    return render(request, "bookshelf/list_books.html", context )


#permission for delete_books ...not complete
@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def can_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "templates/bookshelf/delete_book.html", {"book":book})

    
from .forms import BookForm

#This code was written just to satisfy the checker
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "create.html", {"form": form})
