from datetime import timedelta
from django.core.mail import mail_admins
from .models import AdjunctFacultyMember

# from Notifications.models import Notification


def is_past_due(self):
    return self + timedelta(days=1095) >= self.date.date()


def i9check():
    model = AdjunctFacultyMember.objects.all()
    for f in model:
        i9 = f.I9_completed
        name = f.first_name + " " + f.last_name
        print(name)
        if i9 != 'NA':
            if is_past_due(i9):
                message = 'Hello, ' + name + 's  i9 is greater than 3 years old. please update'
                mail_admins('i9 greater than 3 years', message, fail_silently=False, )
    print("i9 successfully updated")
    # model.objects.filter(I9_greater_than_3_years < 1095).update(f.I9_greater_than_3_years = i9-1)
