import csv
import os
import datetime

from datetime import datetime
from datetime import timedelta
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import UploadFileForm
from CRUD.models import AdjunctFacultyMember, Classes


def upload_file(request):  # view to upload a user device file and parse for adjunct faculty
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # creates a local file copy to read from
            handle_uploaded_file(request.FILES['file'])
            # call function to parse file and import adjunct
            user_import()
            return redirect('import')
        else:
            return render(request, 'Import_Export/import.html', {'form': UploadFileForm(), 'error': "invalid file"})
    # if request is get then return the upload view
    else:
        return render(request, 'Import_Export/import.html', {'form': UploadFileForm()})


def handle_uploaded_file(f):  #creates a local copy of the file passed in by the user
    with open('AdjunctFacultyManagement/static/file.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        f.close()


# parses the file and attempts to add all adjunct faculty contained in the CSV
def user_import():
    with open('AdjunctFacultyManagement/static/file.csv') as f:
        reader = csv.reader(f)
        # try to parse the file. Always delete the file after parsing
        try:
            first_row = True
            for row in reader:
                if not row: break
                # Skip the header row of the csv
                if first_row:
                    first_row = False
                    continue
                # if the employeeID exists then skip this row, they have already been added to the database
                if AdjunctFacultyMember.objects.filter(employeeID=row[4]).exists(): continue
                # parse the current row and attempt to add the faculty member
                adj = AdjunctFacultyMember.objects.get_or_create(
                    a_f_eaf_c_crs_list=row[1],
                    semester=row[2] if contains_num(row[2]) else "--",
                    first_name=get_first_name(row[3]),
                    last_name=get_last_name(row[3]),
                    date_of_birth="2021-10-25",  # FIXME: will csv have DOB?
                    employeeID=row[4],
                    step_rate=get_step_rate(row[5]),
                    I9_completed=i9_completed(row[6]),
                    I9_greater_than_3_years=i9_days_left(row[6]),
                    background_passed=row[8],
                    cv_resume=row[9] if row[9].isdigit() else "0000",
                    masters=has_Masters(row[10]),
                    CTL_notified=ctl_notified(row[11]),
                    address=row[13],
                    city=get_city(row[14]),
                    state=get_state(row[14]),
                    zip=get_zip(row[14]),
                    primary_email=row[15],
                    secondary_email=row[16],
                    primary_phone=get_phone_number(row[17]),
                    secondary_phone=get_phone_number(row[18]),
                    special_conditions_and_comments=row[19],
                    archived=False
                )
                # add the classes for this faculty member
                for c in get_classes(row[12]):
                    Classes.objects.create(
                        adjunct_faculty_member=adj,
                        adj_class=c
                    )
        finally:
            # Always delete the sensitive data file
            f.close()
            os.remove('AdjunctFacultyManagement/static/file.csv')


def parse_date_time(s):
    try:
        s_list = s.split("/")
        s = s_list[0] + "/" + s_list[1] + "/20" + s_list[2]
        return datetime.strptime(s, "%m/%d/%Y")
    except Exception:
        return datetime.strptime("01/01/2000", "%m/%d/%Y")


def i9_completed(s):
    return parse_date_time(s).date()


def ctl_notified(s):
    return parse_date_time(s).date()


def i9_days_left(s):
    parsed_date = parse_date_time(s)
    ret = parsed_date + timedelta(days=1095)
    return ret.date()


def get_classes(s):  # TODO: Separate classes
    return []


def get_phone_number(s):
    phone_list = list(filter(lambda x: x.isdigit(), s))
    phone_str = ""
    for num in phone_list: phone_str += num
    return phone_str


def get_city(s):
    lst = s.split(", ")
    return lst[0]


def get_state(s):
    if len(s) == 0 or "NA" in s: return "NA"
    lst = s.split(", ")
    if len(lst) < 2: return "NA"
    lst = lst[1].split(" ")
    return lst[0]


def get_zip(s):
    if len(s) == 0 or "NA" in s: return 00000
    lst = s.split(", ")
    if len(lst) < 2: return 00000
    lst = lst[1].split(" ")
    return lst[1]


def has_Masters(s):
    if len(s) == 0 or "NA" in s: return "N"
    return "Y"


def get_step_rate(s):
    steps = {"1": "1", "2": "2", "3": "3"}
    return steps.get(s, "f")


def get_first_name(s):
    if len(s) == 0 or "NA" in s: return "NA"
    lst = s.split(",")
    return lst[1]


def get_last_name(s):
    if len(s) == 0 or "NA" in s: return "NA"
    lst = s.split(",")
    return lst[0]


def contains_num(s):
    return any(i.isdigit() for i in s)
