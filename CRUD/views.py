from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AdjunctFacultyMember, Classes
from .forms import AdjunctForm
from django_cryptography.fields import *



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


# List of adjunct Fields For crud_read view
adjunctFields = {
    "A, F, EAF, C-CRS-LIST": "a_f_eaf_c_crs_list",
    "Semester": "semester",
    "First Name": "first_name",
    "Last Name": "last_name",
    "Date of Birth": "date_of_birth",
    "Employee ID": "employeeID",
    "Step Rate": "step_rate",
    "I9 Completed": "I9_completed",
    "I9 Greater Than 3 Years": "I9_greater_than_3_years",
    "Background Passed": "background_passed",
    "CV/Resume": "cv_resume",
    "Masters": "masters",
    "CTL Notified": "CTL_notified",
    "Address": "address",
    "City": "city",
    "State": "state",
    "Zip": "zip",
    "Primary Email": "primary_email",
    "Secondary Email": "secondary_email",
    "Primary Phone": "primary_phone",
    "Secondary Phone": "secondary_phone",
    "Special Conditions and Comments": "special_conditions_and_comments",
}

# List for option field 1 in read_view
option1Fields = {
    "First Name": "first_name",
    "Last Name": "last_name",
    "Employee ID": "employeeID",
}

# List for option field 2 in read)view
option2Fields = {
    "Select All": "all",
    "Semester": "semester",
    "First Name": "first_name",
    "Last Name": "last_name",
    "Employee ID": "employeeID",
    "Step Rate": "step_rate",
    "I9 Completed": "I9_completed",
    "I9 Greater Than 3 Years": "I9_greater_than_3_years",
    "Background Passed": "background_passed",
    "CV/Resume": "cv_resume",
    "Masters": "masters",
    "CTL Notified": "CTL_notified",
    "Address": "address",
    "City": "city",
    "State": "state",
    "Zip": "zip",
    "Primary Email": "primary_email",
    "Secondary Email": "secondary_email",
    "Primary Phone": "primary_phone",
    "Secondary Phone": "secondary_phone"
}


# Redirects to Search and View page in menu bar
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
            option2 = request.GET.getlist('option2')
            tableHeaders = {}
            for option in option2:
                tableHeaders[option] = adjunctFields[option]

            if "Select All" in tableHeaders:
                tableHeaders = adjunctFields
                retFieldsList = adjunctFields.values()
            else:
                # Get corresponding model names for table headers
                retFieldsList = tableHeaders.values()

            if includeArchives is None:
                results = AdjunctFacultyMember.objects.all().filter(**searchFilter).filter(archived=False).order_by(
                    'first_name')
            else:
                results = AdjunctFacultyMember.objects.all().filter(**searchFilter).order_by('first_name')

            results = results.values(*retFieldsList)
            

            if not results:
                tableHeaders = {}
            print(tableHeaders)
            if not tableHeaders:
                tableHeaders = adjunctFields

            # return render(request, 'CRUD/read_view.html',
            #               {'results': results, 'fields': adjunctFields, 'option1Fields': option1Fields,
            #                'option2Fields': option2Fields, 'tableHeaders': tableHeaders})

            return JsonResponse({'results': list(results), 'fields': list(adjunctFields), 'option1Fields': list(option1Fields),
                           'option2Fields': list(option2Fields), 'tableHeaders': tableHeaders, 'sr_choices': list(AdjunctFacultyMember.sr_choices), 'bg_choices': list(AdjunctFacultyMember.bg_choices), 'masters_choices': list(AdjunctFacultyMember.masters_choices), 'a_f_eaf_c_crs_choices': list(AdjunctFacultyMember.a_f_eaf_c_crs_choices)}, status=200)

        return render(request, 'CRUD/read_view.html', {'option1Fields': option1Fields, 'option2Fields': option2Fields})


# Redirects to Search and Edit page in menu bar
@login_required
def crud_search_edit(request):
    if request.method == 'GET':
        return render(request, 'CRUD/edit_view.html')


# Redirects to add rows page in menu bar
@login_required
def crud_add_rows(request):
    uniqClasses = set()

    for c in list(Classes.objects.all().values("adj_class")):
        values = c.values()
        for value in values:
            uniqClasses.add(value)

    if request.method == 'POST':
        form = AdjunctForm(request.POST, request.FILES)

        if form.is_valid():
            adj = form.save()
            classes = request.POST.getlist('option2')
            for c in classes:
                newClass = Classes(adjunct_faculty_member=adj, adj_class=c)
                newClass.save()

            return redirect('add_rows')
        else:
            print("Form wasnt valid")
            return render(request, 'CRUD/add_rows.html', {'form': form, 'error': "unable to add", 'classes': uniqClasses})
    if request.method == 'GET':
        form = AdjunctForm()
        return render(request, 'CRUD/add_rows.html', {'form': form, 'uniqClasses': uniqClasses})


# Redirects to import page in menu bar
@login_required
def user_import(request):
    if request.method == 'GET':
        return render(request, 'Import_Export/import.html')



# Redirects to Notifications page in menu bar
@login_required
def user_notifications(request):
    if request.method == 'GET':
        return render(request, 'Notifications/notifications.html')

