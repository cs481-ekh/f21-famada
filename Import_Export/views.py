from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from CRUD.models import AdjunctFacultyMember, Classes


# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        print("posted!!!")
        print(request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid form")
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        UploadFileForm()
        return render(request, 'Import_Export/import.html', {'form': UploadFileForm()})


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# Redirects to import page in menu bar
def user_import(f):
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
