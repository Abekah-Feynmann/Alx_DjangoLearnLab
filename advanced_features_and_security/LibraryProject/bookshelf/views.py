from django.shortcuts import render
from django.contrib.auth.models import Permission

# Create your views here.
#Defining Custom Permissions

#get permissiion
permission = Permission.objects.filter(
    codename__in=['can_view', 'can_edit', 'can_create', 'can_delete'])
CustomUser.user_permissions.add(permission)