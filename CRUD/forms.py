from django import forms
from django.forms.models import ModelForm
from .models import AdjunctFacultyMember
from .models import Classes



class DateInput(forms.DateInput):
    input_type = 'date'


class AdjunctForm(forms.ModelForm):
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    I9_completed = forms.CharField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    CTL_notified = forms.CharField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    primary_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone'}))
    secondary_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone'}))

    class Meta:
        model = AdjunctFacultyMember
        fields = (
            'a_f_eaf_c_crs_list', 'semester', 'employeeID', 'first_name', 'last_name', 'date_of_birth', 'step_rate',
            'I9_completed', 'background_passed', 'cv_resume',
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
    fields = (
        'adjunct_faculty_member', 'adj_class'
    )

