from .models import AdjunctFacultyMember
from .models import Classes
from datetime import datetime


def timeOfDay():
    print('hello')


def i9check():
    model = AdjunctFacultyMember.objects.all()
    for each in model:
        i9 = model.I9_greater_than_3_years
        if i9 != 'NA':
            i9 -= 1
            i9.save()
        #  if(i9 <= 0):
        # notify()
        # model.objects.filter(I9_greater_than_3_years < 1095).update(f.I9_greater_than_3_years = i9-1)
