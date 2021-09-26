from django.db import models
from phone_field import PhoneField

# Create your models here.
class AdjunctFacultyMember(models.Model):
    a_f_eaf_c_crs_list = models.CharField(max_length=3)
    semester = models.CharField(max_lenght=4)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    employeeID = models.IntegerField(max_length=30)
    I9_completed = models.DateField()
    I9_greater_than_3_years = models.IntegerField
    background_passed = models.BooleanField
    cv_resume = models.CharField(max_length=4)
    masters = models.CharField(max_length=30)
    CTL_notified = models.DateField()
    classes = models.CharField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField(max_length=2)
    zip = models.IntegerField()
    primary_email = models.EmailField()
    secondary_email = models.EmailField()
    primary_phone = PhoneField(blank=True, help_text='Primary phone number')
    secondary_phone = PhoneField(blank=True, help_text='Secondary phone number')
    special_conditions_and_comments = models.CharField()
    semesters_taught = models.CharField()





