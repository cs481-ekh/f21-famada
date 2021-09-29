from django import forms
from .models import AdjunctFacultyMember


class AdjunctForm(forms.ModelForm):
    class Meta:
        model = AdjunctFacultyMember
        fields = (
            'a_f_eaf_c_crs_list', 'semester', 'first_name', 'last_name', 'employeeID',
            'I9_completed', 'I9_greater_than_3_years', 'background_passed', 'cv_resume',
            'masters', 'CTL_notified', 'classes', 'address', 'city', 'state', 'zip',
            'primary_email', 'secondary_email', 'primary_phone', 'secondary_phone',
            'special_conditions_and_comments', 'semesters_taught'
        )
