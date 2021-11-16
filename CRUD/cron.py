from datetime import timedelta, datetime
from django.core.mail import mail_admins
from .models import AdjunctFacultyMember

from Notifications.models import Notification


def parseDate(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def i9check():
    for obj in AdjunctFacultyMember:
        for f in obj.objects.all():  # loops through table
            name = f.first_name + " " + f.last_name
            print(name)
            if i9 != 'NA':  # checks null
                i9s = f.I9_completed
                print(i9s)
                i9 = datetime.strptime(i9s, "%Y-%m-%d").date()
                print(i9)
                daysahead = i9 + timedelta(days=1095)
                if daysahead >= datetime.now():
                    print("i9 > 3 years")
                    message = 'Hello, ' + name + 's  i9 is greater than 3 years old. please update'
                    mail_admins('i9 greater than 3 years', message, fail_silently=False, )
    print("i9 successfully updated")
    # model.objects.filter(I9_greater_than_3_years < 1095).update(f.I9_greater_than_3_years = i9-1)
