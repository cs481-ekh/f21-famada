from django import forms
from django.forms.models import ModelForm
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = 'message', 'date'