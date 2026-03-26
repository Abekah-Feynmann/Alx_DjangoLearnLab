from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification

# Create your views here.
class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient= self.request.user)


