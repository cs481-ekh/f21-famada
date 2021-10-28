from django import forms
from django.forms.models import ModelForm
from .models import AdjunctFacultyMember
from .models import Classes
from .models import Notification


class DateInput(forms.DateInput):
    input_type = 'date'


class AdjunctForm(forms.ModelForm):
    class Meta:
        model = AdjunctFacultyMember
        fields = (
            'a_f_eaf_c_crs_list', 'semester', 'first_name', 'last_name', 'date_of_birth', 'employeeID', 'step_rate',
            'I9_completed', 'I9_greater_than_3_years', 'background_passed', 'cv_resume',
            'masters', 'CTL_notified', 'address', 'city', 'state', 'zip',
            'primary_email', 'secondary_email', 'primary_phone', 'secondary_phone',
            'special_conditions_and_comments', 'archived'
        )
        # widgets = {
        #     'date_of_birth' : DateInput(),
        #     'I9_completed'  : DateInput(),
        #     'CTL_notified'  : DateInput(),
        # }


class ClassForm(forms.ModelForm):
    model = Classes
    fields = 'class_name'


class NotificationForm(forms.ModelForm):
    model = Notification
    fields = 'message', 'date'
