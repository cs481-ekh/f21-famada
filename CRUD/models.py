from django.db import models
from phone_field import PhoneField


# Create your models here.
class AdjunctFacultyMember(models.Model):
    a_f_eaf_c_crs_choices = {
        ('A', 'A'),
        ('F', 'F'),
        ('EAF', 'EAF'),
        ('C', 'C'),
        ('CRS', 'CRS')  # maybe used?
    }
    background_choices = {
        ('P', 'pass'),
        ('NA', 'NA'),
        (' ', ' '),
        ('--', '--')
    }
    a_f_eaf_c_crs_list = models.CharField(null=False, blank=False, choices=a_f_eaf_c_crs_choices, max_length=3)
    semester = models.CharField(default='--', max_length=4)
    first_name = models.CharField(null=False, blank=False, max_length=30)
    last_name = models.CharField(null=False, blank=False, max_length=30)
    employeeID = models.IntegerField(null=False, blank=False)
    step_rate_dept = models.CharField(null=False, blank=False, max_length=10)
    I9_completed = models.DateField(null=False, blank=False, default='NA')
    I9_greater_than_3_years = models.IntegerField(null=False, blank=False, default='NA')
    background_passed = models.CharField(null=False, blank=False, default='NA', choices=background_choices,  max_length=2)
    cv_resume = models.CharField(default='NA', max_length=4)
    masters = models.CharField(default='NA', max_length=30)
    CTL_notified = models.DateField(null=False, blank=False, default='NA')
    classes = models.TextField(null=False, blank=False, )
    address = models.CharField(null=False, blank=False, max_length=50)
    city = models.CharField(null=False, blank=False, max_length=20)
    state = models.CharField(null=False, blank=False, max_length=2)
    zip = models.IntegerField(null=False, blank=False, )
    primary_email = models.EmailField(null=False, blank=False)
    secondary_email = models.EmailField()
    primary_phone = PhoneField(null=False, blank=False,  help_text='Primary phone number')
    secondary_phone = PhoneField(default='NA', blank=True, help_text='Secondary phone number')
    special_conditions_and_comments = models.TextField()
    semesters_taught = models.TextField()
