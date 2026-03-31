from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification

# Create your views here.
#Provides a view for the list of notifications
class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient= self.request.user).order_by("-timestamp")

    @action(detail=True, methods=["post"])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({"status":"marked as read"})

    @action(detail=True, method=["post"])
    def mark_all_as_read(self, request):
        notification = self.get_queryset().update(is_read=True)
    
        return Response({"status":"all marked as read"})
    
    @action(detail=True, method=["get"])
    def unread(self, request):
        notification = self.get_queryset().filter(is_read=False)
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)



