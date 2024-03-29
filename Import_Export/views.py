import csv
import os
import datetime

from datetime import datetime
from datetime import timedelta
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import FilesModel
from CRUD.models import AdjunctFacultyMember, Classes


# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        print("posted!!!")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user_import()
            return redirect('import')
    else:
        return render(request, 'Import_Export/import.html', {'form': UploadFileForm()})


# Redirects to import page in menu bar
def user_import():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path.replace("Import_Export", "")+"media/"+FilesModel.objects.all().values()[0]['csv']
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            first_row = True
            for row in reader:
                if not row or not row[0]: break

                if first_row:
                    first_row = False
                    continue

                if not row[4]: row[4] = 0
                if AdjunctFacultyMember.objects.filter(employeeID=row[4]).exists(): continue

                adj = AdjunctFacultyMember.objects.get_or_create(
                    a_f_eaf_c_crs_list=row[1],
                    semester=row[2] if contains_num(row[2]) else "--",
                    first_name=get_first_name(row[3]),
                    last_name=get_last_name(row[3]),
                    employeeID=row[4],
                    date_of_birth=parse_date_time([5]).date(),
                    step_rate=get_step_rate(row[6]),
                    I9_completed=i9_completed(row[7]),
                    I9_greater_than_3_years=i9_days_left(row[8]),
                    background_passed=row[9],
                    cv_resume=row[10] if row[10].isdigit() else "0000",
                    masters=has_Masters(row[11]),
                    CTL_notified=ctl_notified(row[12]),
                    address=row[14],
                    city=get_city(row[15]),
                    state=get_state(row[15]),
                    zip=get_zip(row[15]),
                    primary_email=row[16],
                    secondary_email=row[17],
                    primary_phone=get_phone_number(row[18]),
                    secondary_phone=get_phone_number(row[19]),
                    special_conditions_and_comments=row[20],
                    archived=False
                )

                for c in get_classes(row[12]):
                    Classes.objects.create(
                        adjunct_faculty_member=adj,
                        adj_class=c
                    )
                # if not first_row:
                #     break
        finally:
            # Always delete the sensitive data file
            f.close()
            os.remove(file_path)
            FilesModel.objects.all().delete()


def parse_date_time(s):
    try:
        sList = s.split("/")
        s = sList[0] + "/" + sList[1] + "/20" + sList[2]
        return datetime.strptime(s, "%m/%d/%Y")
    except:
        return datetime.strptime("01/01/2000", "%m/%d/%Y")


def i9_completed(s):
    return parse_date_time(s).date()


def ctl_notified(s):
    return parse_date_time(s).date()


def i9_days_left(s):
    parsedDate = parse_date_time(s)
    ret = parsedDate + timedelta(days=1095)
    return ret.date()


def get_classes(s):  # TODO: Separate classes
    return []


def get_phone_number(s):
    lst = list(filter(lambda x: x.isdigit(), s))
    str = ""
    for l in lst: str += l

    return str


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
    return lst[1][:4]


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
