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


adjunctFields = {
    "A_F_EAF_C_CRS_LIST": "a_f_eaf_c_crs_list",
    "Semester": "semester",
    "First Name": "first_name",
    "Last Name": "last_name",
    "Employee ID": "employeeID",
    "I9 Completed": "I9_completed",
    "I9 Greater Than 3 Years": "I9_greater_than_3_years",
    "Background Passed": "background_passed",
    "CV/Resume": "cv_resume",
    "Masters": "masters",
    "CTL Notified": "CTL_notified",
    "Classes": "classes",
    "Address": "address",
    "City": "city",
    "State": "state",
    "Zip": "zip",
    "Primary Email": "primary_email",
    "Secondary Email": "secondary_email",
    "Primary Phone": "primary_phone",
    "Secondary Phone": "secondary_phone",
    "Special Conditions and Comments": "special_conditions_and_comments",
    "Semesters Taught": "semesters_taught",
    "Archived": "archived"
}

option1Fields = {
    "First Name": "first_name",
    "Last Name": "last_name",
    "Employee ID": "employeeID",
}

option2Fields = {
    "Select All": "all",
    "First Name": "first_name",
    "Last Name": "last_name",
}


@login_required
def crud_read(request):
    if request.method == 'GET':
        # Check if this is a page load or a search query
        if request.GET.get("option1"):
            # Take in arguments from the GET
            option1 = request.GET.get('option1') + "__icontains"
            searchString = request.GET.get('searchString')
            searchFilter = {option1: searchString}
            includeArchives = request.GET.get('archive')

            # Get selected options from option 2 list
            tableHeaders = request.GET.getlist('option2')

            allSelected = False
            if "Select All" in tableHeaders:
                tableHeaders = adjunctFields.keys()
                allSelected = True
                retFieldsList = adjunctFields.values()
            else:
                # Get corresponding model names for table headers
                retFieldsList = [option2Fields.get(key) for key in tableHeaders]

            if includeArchives is None:
                results = AdjunctFacultyMember.objects.all().filter(**searchFilter).filter(archived=False).order_by(
                    'first_name')
            else:
                results = AdjunctFacultyMember.objects.all().filter(**searchFilter).order_by('first_name')


            results = results.values(*retFieldsList)

            if not results:
                tableHeaders = []
            print(results)
            return render(request, 'CRUD/read_view.html',
                          {'results': results, 'fields': adjunctFields, 'option1Fields': option1Fields,
                           'option2Fields': option2Fields, 'tableHeaders': tableHeaders})

        return render(request, 'CRUD/read_view.html', {'option1Fields': option1Fields, 'option2Fields': option2Fields})
