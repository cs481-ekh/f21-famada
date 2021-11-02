from .models import AdjunctFacultyMember
from .models import Classes
from .models import Notification
from datetime import datetime


def timeOfDay():
    print('today is' : {}'.format(datetime.now()))

def i9check():
    model = AdjunctFacultyMember
    for f in model._meta.fields:
         i9 = f.i9_greater_than_3_years
         model.objects.filter(i9_greater_than_3_years < 1095).update(f.i9_greater_than_3_years = i9+1)

