from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AdjunctFacultyMember, Classes
from Notifications.models import Notification
from .forms import AdjunctForm
from django.views.decorators.csrf import csrf_exempt



def user_login(request):
    # if user is already logged in the redirect to landing page
    if request.user.is_authenticated:
        return redirect('search')
    # if request is a get return the login page
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # attempt to authenticate the user
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        # if user is non then authentication failed
        if user is None:
            # return an error
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
        else:
            # authentication was a success, login the user
            login(request, user)
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
    # get all of the unread notifications
    unread_notifications = len(Notification.objects.all().filter(isRead=False))

    if request.method == 'GET':
        # Check if this is a page load or a search query
        if request.GET.get("option1"):
            # Take in arguments from the GET
            option1 = request.GET.get('option1') + "__icontains"
            search_string = request.GET.get('searchString')
            search_filter = {option1: search_string}
            include_archives = request.GET.get('archive')

            # Get selected options from option 2 list
            option2 = request.GET.getlist('option2')
            if "Select All" in option2:
                option2.remove("Select All")

            # create a dictionary of table headers to use in view
            table_headers = {}
            for option in option2:
                table_headers[option] = adjunctFields[option]

            # Get corresponding model names for table headers
            ret_fields_list = list(table_headers.values())
            ret_fields_list.append("employeeID")

            # check if the user wants archived personnel include if so
            if include_archives is None:
                results = AdjunctFacultyMember.objects.all().filter(**search_filter).filter(archived=False).order_by(
                    'first_name')
            else:
                results = AdjunctFacultyMember.objects.all().filter(**search_filter).order_by('first_name')

            results = results.values(*ret_fields_list)

            if not results:
                table_headers = {}
            if not table_headers:
                table_headers = adjunctFields

            return JsonResponse(
                {'results': list(results), 'fields': list(adjunctFields), 'option1Fields': list(option1Fields),
                 'option2Fields': list(option2Fields), 'tableHeaders': table_headers,
                 'sr_choices': list(AdjunctFacultyMember.sr_choices),
                 'bg_choices': list(AdjunctFacultyMember.bg_choices),
                 'masters_choices': list(AdjunctFacultyMember.masters_choices),
                 'a_f_eaf_c_crs_choices': list(AdjunctFacultyMember.a_f_eaf_c_crs_choices),
                 'unreadNotifications': unread_notifications}, status=200)

        # if no option is selected we cant search so we return the default view
        return render(request, 'CRUD/read_view.html', {'option1Fields': option1Fields, 'option2Fields': option2Fields,
                                                       'unreadNotifications': unread_notifications})
    # if its a post we are deleting an adjunct
    else:
        adjunct_ID = request.POST.get('rowID')
        adjunct = AdjunctFacultyMember.objects.get(employeeID=adjunct_ID)
        # delete the employee
        adjunct.delete()
        # redirect back to the updated search view
        return redirect('search')

      
# Redirects to add rows page in menu bar
@login_required
def crud_add_rows(request):
    # create a unique set of class names
    uniq_classes = set()
    # populate the set
    for c in list(Classes.objects.all().values("adj_class")):
        values = c.values()
        for value in values:
            uniq_classes.add(value)

    # if its a post we are creating a new adjunct and their classes
    if request.method == 'POST':
        # create an instance of the adjunct form
        form = AdjunctForm(request.POST, request.FILES)
        # validate form, if valid save the adjunct and attempt to save their classes
        if form.is_valid():
            adj = form.save()
            classes = request.POST.getlist('option2')
            # Try to save all of the adjuncts classes. If unable to save continue onto the next class
            for c in classes:
                try:
                    new_class = Classes(adjunct_faculty_member=adj, adj_class=c)
                    new_class.save()
                except Exception:
                    continue
            # Redirect back to the add view
            form = AdjunctForm()
            return render(request, 'CRUD/add_rows.html',
                          {'success': True, 'form': form})
        else:
            # return an error if unable to add an adjunct
            print("form invalid")
            print(form.errors.as_json())
            return render(request, 'CRUD/add_rows.html',
                          {'form': form, 'success': False, 'error': "unable to add", 'errorList':form.errors.as_json(), 'classes': uniq_classes})
    # if the request is a GET then return a default adjunct form
    else:
        form = AdjunctForm()
        return render(request, 'CRUD/add_rows.html', {'form': form, 'uniqClasses': uniq_classes})


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
