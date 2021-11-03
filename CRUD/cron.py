from .models import AdjunctFacultyMember
from .models import Classes
from .models import Notification
from datetime import datetime


def timeOfDay():
    print('hello')


def i9check():
    model = AdjunctFacultyMember
    for f in model.I9_greater_than_3_years:
        i9 = f.I9_greater_than_3_years
        if i9 != 'NA':
            i9 = i9 - 1
            i9.save()
        #  if(i9 <= 0):
        # notify()
        # model.objects.filter(I9_greater_than_3_years < 1095).update(f.I9_greater_than_3_years = i9-1)
