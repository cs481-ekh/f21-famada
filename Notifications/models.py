from django.db import models
from datetime import datetime

# Create your models here.
class Notification(models.Model):
    message = models.TextField()
    date = models.DateField(default=datetime.now)
    isRead = models.BooleanField()