from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.

def user_login(request):
    # if user is already logged in the redirect to landing page
    if request.user.is_authenticated:
        return redirect('search')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
        else:
            login(request, user)
            if 'next' in request.POST:
                # check for case next is logout? else redirect to next
                return redirect(request.POST.get('next'))
            return redirect('search')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

#Redirects to Search and View page in menu bar
@login_required
def crud_read(request):
    if request.method == 'GET':
        return render(request, 'CRUD/read_view.html')

#Redirects to Search and Edit page in menu bar
@login_required
def crud_search_edit(request):
    if request.method == 'GET':
            return render(request, 'CRUD/edit_view.html')

#Redirects to add rows page in menu bar
@login_required
def crud_add_rows(request):
    if request.method == 'GET':
            return render(request, 'CRUD/add_rows.html')


#Redirects to import page in menu bar
@login_required
def user_import(request):
    if request.method == 'GET':
            return render(request, 'Import_Export/import.html')

#Redirects to Notifications page in menu bar
@login_required
def user_notifications(request):
    if request.method == 'GET':
            return render(request, 'Notifications/notifications.html')



        
