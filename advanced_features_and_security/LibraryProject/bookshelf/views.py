from django.shortcuts import render
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from relationship_app.models import Library



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

        




    

