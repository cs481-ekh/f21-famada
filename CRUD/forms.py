from django import forms
from .models import AdjunctFacultyMember
from .models import Classes


class AdjunctForm(forms.ModelForm):
    class Meta:
        model = AdjunctFacultyMember
        fields = (
            'a_f_eaf_c_crs_list', 'semester', 'first_name', 'last_name', 'employeeID', 'step_rate',
            'I9_completed', 'I9_greater_than_3_years', 'background_passed', 'cv_resume',
            'masters', 'CTL_notified', 'address', 'city', 'state', 'zip',
            'primary_email', 'secondary_email', 'primary_phone', 'secondary_phone',
            'special_conditions_and_comments', 'archived'
        )


class ClassForm(forms.ModelForm):
    model = Classes
    fields = 'class_name'
