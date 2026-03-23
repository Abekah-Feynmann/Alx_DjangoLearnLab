from django.db import models
from django.conf import settings
from django.contrib.contentypes.models import ContentType
from django.contrib.contentypes.fields import GenericForeignKey

# Create your models here.

#A notification model.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verb = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField()
