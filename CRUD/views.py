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

adjunctFields = [
    "a_f_eaf_c_crs_list ",
    "semester",
    "first_name",
    "last_name",
    "employeeID",
    "I9_completed",
    "I9_greater_than_3_years",
    "background_passed",
    "cv_resume",
    "masters",
    "CTL_notified",
    "classes",
    "address",
    "city",
    "state",
    "zip",
    "primary_email",
    "secondary_email",
    "primary_phone",
    "secondary_phone",
    "special_conditions_and_comments",
    "semesters_taught"
]

option1Fields = {
    "First Name":"first_name",
    "Last Name":"last_name",
    "Employee ID":"employeeID",
}

option2Fields = {
    "Select All":"all",
    "First Name":"first_name",
    "Last Name":"last_name",
}

@login_required
def crud_read(request):
    if request.method == 'GET':
        # Check if this is a page load or a search query
        if request.GET.get("option1"):
            option1 = request.GET.get('option1')+"__icontains"
            searchString = request.GET.get('searchString')
            includeArchives = request.GET.get('archive')
            searchFilter = {option1:searchString}

            print(request.GET.getlist('option2'))

            if includeArchives is None:
                results = AdjunctFacultyMember.objects.all().filter(**searchFilter).filter(archived=False).order_by('first_name')
            else:
                results = AdjunctFacultyMember.objects.all().filter(**searchFilter).order_by('first_name')

            return render(request, 'CRUD/read_view.html',
                          {'results': results, 'fields': adjunctFields, 'option1Fields': option1Fields,'option2Fields': option2Fields})

        return render(request, 'CRUD/read_view.html', {'option1Fields': option1Fields,'option2Fields': option2Fields})


