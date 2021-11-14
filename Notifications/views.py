from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import Notification
from .forms import NotificationForm

# Create your views here.

# Redirects to Notifications page in menu bar

notification_fields = {
    "ID": "id",
    "Message": "message",
    "Read": "isRead",
    "Date": "date"
}


@login_required
def user_notifications(request):
    data = Notification.objects.all()
    notif_info = {
        "notifications": data
    }
    if request.method == 'GET':
        return render(request, 'Notifications/notifications.html', notif_info)


@login_required
def update_view(request):
    context = {}

    obj = get_object_or_404(Notification)

    form = NotificationForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("Notifications")

    context["form"] = form

    return render(request, "Notifications")


@login_required
def delete_view(request):
    obj = get_object_or_404(Notification)

    if request.method == "POST":
        obj.delete()
        return redirect("Notifications")

    return render(request, "Notifications")

@login_required
def isRead(request):
    context = {}

    obj = get_object_or_404(Notification)

    form = NotificationForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.isRead = True
        obj.save()

    context["form"] = form

    return render(request, "Notifications")
