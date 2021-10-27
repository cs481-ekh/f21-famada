import csv

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AdjunctFacultyMember, Classes
from .forms import AdjunctForm
from django.views.decorators.csrf import csrf_exempt


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
@csrf_exempt
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
            if "Select All" in option2:
                option2.remove("Select All")
            tableHeaders = {}
            for option in option2:
                tableHeaders[option] = adjunctFields[option]

            if "Select All" in tableHeaders:
                tableHeaders = adjunctFields
                retFieldsList = adjunctFields.values()
            else:
                # Get corresponding model names for table headers
                retFieldsList = list(tableHeaders.values())
                retFieldsList.append("employeeID")
                print(retFieldsList)

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
            return JsonResponse(
                {'results': list(results), 'fields': list(adjunctFields), 'option1Fields': list(option1Fields),
                 'option2Fields': list(option2Fields), 'tableHeaders': tableHeaders}, status=200)

        return render(request, 'CRUD/read_view.html', {'option1Fields': option1Fields, 'option2Fields': option2Fields})
    else:
        adjunct_ID = request.POST.get('rowID')
        adjunct = AdjunctFacultyMember.objects.get(employeeID=adjunct_ID)
        adjunct.delete()
        return redirect('search')


# Redirects to Search and Edit page in menu bar
@login_required
def crud_search_edit(request):
    if request.method == 'GET':
        return render(request, 'CRUD/edit_view.html')


# Redirects to add rows page in menu bar
@login_required
def crud_add_rows(request):
    form = AdjunctForm()
    if request.method == 'GET':
        return render(request, 'CRUD/add_rows.html', {'form': form})


# Redirects to import page in menu bar
@login_required
def user_import(request):
    if request.method == 'GET':
        return render(request, 'Import_Export/import.html')
    else:
        with open('../Test Dataset for COEN project.csv') as f:
            reader = csv.reader(f)

            for row in reader:
                adj = AdjunctFacultyMember.objects.create(
                    a_f_eaf_c_crs_list=row[1],
                    semester=row[2] if contains_num(row[2]) else "--",
                    first_name=get_first_name(row[3]),
                    last_name=get_last_name(row[3]),
                    date_of_birth=None,  # TODO: add valid birth date
                    employeeID=row[4],
                    step_rate=get_step_rate([5]),
                    I9_completed=row[6],
                    I9_greater_than_3_years=1095,  # TODO: add valid greater than based on I9 completed
                    background_passed=get_I9_Pass_Fail(row[8]),
                    cv_resume=row[9] if row[9].isdigit() else "0000",
                    masters=has_Masters(row[10]),
                    CTL_notified=row[11],  # TODO: Add date parser
                    address=row[13],
                    city=get_city(row[14]),
                    state=get_state(row[14]),
                    zip=get_zip(row[14]),
                    primary_email=row[15],
                    secondary_email=row[16] if len(row[16]) != 0 else None,
                    primary_phone=get_phone_number(row[17]),
                    secondary_phone=get_phone_number(row[18]),
                    special_conditions_and_comments=row[19]
                )

                for c in row[12].split(","):  # TODO: Fix this
                    Classes.objects.create(
                        adjunct_faculty_member=adj,
                        adj_class=c
                    )


def get_phone_number(s):  # TODO: Make sure this works properly
    return filter(lambda x: x.isdigit(), s)


def get_city(s):
    lst = s.split(", ")
    return lst[0]


def get_state(s):
    lst = s.split(", ")
    lst = lst[1].split(" ")
    return lst[0]


def get_zip(s):
    lst = s.split(", ")
    lst = lst[1].split(" ")
    return lst[1]


def has_Masters(s):
    if len(s) == 0 or s == "NA": return "No"
    return "Yes"  # TODO: make this more accurate


def get_I9_Pass_Fail(s):
    i9 = {"P": "pass", "NA": "NA", "F": "fail"}
    return i9.get(s, default="NA")


def get_step_rate(s):
    steps = {"1": "step 1", "2": "step 2", "3": "step 3"}
    return steps.get(s, default="faculty")


def get_first_name(s):
    lst = s.split(",")
    return lst[1]


def get_last_name(s):
    lst = s.split(",")
    return lst[0]


def contains_num(s):
    return any(i.isdigit() for i in s)


# Redirects to Notifications page in menu bar
@login_required
def user_notifications(request):
    if request.method == 'GET':
        return render(request, 'Notifications/notifications.html')
