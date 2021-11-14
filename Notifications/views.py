from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from Notifications.models import Notification
from .forms import NotificationForm

# Create your views here.

#Redirects to Notifications page in menu bar
@login_required
def user_notifications(request):
    data = Notification.objects.all()
    # gets all notifications from database as stores in a variable that can
    # be used in html as notifications
    notif_info = {
        "notifications": data
    }
    if request.method == 'GET':
            return render(request, 'Notifications/notifications.html', notif_info)