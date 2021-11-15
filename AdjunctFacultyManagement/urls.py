"""AdjunctFacultyManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CRUD import views as crud_views
from Import_Export import views as impex_views
from Notifications import views as notif_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud_views.user_login, name='login'),
    path('logout/', crud_views.user_logout, name='logout'),
    path('search/', crud_views.crud_read, name='search'), #Search and View page
    path('search_edit/', crud_views.crud_search_edit, name='search_edit'), #Search and Edit page
    path('add/', crud_views.crud_add_rows, name='add_rows'), #Add Rows page
    path('import/', impex_views.upload_file, name='import'), #Import files page
    path('notifications/', notif_views.user_notifications, name='notifications'), #Notifications page
]
