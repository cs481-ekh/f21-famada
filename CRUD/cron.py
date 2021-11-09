from .models import AdjunctFacultyMember
from .models import Classes
from datetime import datetime
from django.core.mail import mail_admins


def timeOfDay():
    print('hello')


def i9check():
    model = AdjunctFacultyMember.objects.all()
    for f in model:
        i9 = model.I9_greater_than_3_years
        name = model.first_name + " " + model.last_name
        if i9 != 'NA':
            i9 -= 1
            i9.save()
        if i9 <= 0:
            message = 'Hello, ' + name + ' i9 is greater than 3 years old. please update'
            mail_admins('i9 greater than 3 years', message, fail_silently=False, )
        # model.objects.filter(I9_greater_than_3_years < 1095).update(f.I9_greater_than_3_years = i9-1)
