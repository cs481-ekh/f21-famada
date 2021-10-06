from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import AdjunctFacultyMember

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


@login_required
def crud_read(request):
    if request.method == 'GET':
        # Check if this is a page load or a search query
        if request.GET.get("option1"):
            option1 = request.GET['option1']+"__icontains"
            searchString = request.GET['searchString']
            searchFilter = {option1:searchString}

            results = AdjunctFacultyMember.objects.all().filter(**searchFilter).order_by('first_name')
            return render(request, 'CRUD/read_view.html', {'results': results})

        return render(request, 'CRUD/read_view.html')


