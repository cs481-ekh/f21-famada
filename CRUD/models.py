from datetime import datetime

from django.db import models
from phone_field import PhoneField
from django_cryptography.fields import encrypt


# Create your models here.


class AdjunctFacultyMember(models.Model):
    a_f_eaf_c_crs_choices = {
        ('A', 'A'),
        ('F', 'F'),
        ('EAF', 'EAF'),
        ('C', 'C'),
        ('CRS', 'CRS')  # maybe used?
    }
    masters_choices = {
        ("Y", 'Yes'),
        ('N', 'No')
    }
    bg_choices = {  # background choices
        ('NA', 'NA'),
        ('P', 'pass'),
        ('F', 'fail')
    }
    sr_choices = {  # step rate choices
        ('1', 'step 1'),
        ('2', 'step 2'),
        ('3', 'step 3'),
        ('F', 'faculty')
    }
    a_f_eaf_c_crs_list = models.CharField(null=False, blank=False, choices=a_f_eaf_c_crs_choices, max_length=3)
    semester = models.CharField(max_length=4, help_text="please enter SP, FA, or SU followed by a 2 digit year. (ex. SP21)")
    first_name = models.CharField(null=False, blank=False, max_length=30)
    last_name = models.CharField(null=False, blank=False, max_length=30)
    date_of_birth = models.DateField(null=False, blank=False, default=datetime.now)
    employeeID = models.IntegerField(null=False, blank=False, unique=True, primary_key=True)
    step_rate = models.CharField(null=False, blank=False, choices=sr_choices, max_length=10, default='step 1')
    I9_completed = models.DateField(null=False, blank=False)
    I9_greater_than_3_years = models.IntegerField(null=True, blank=True, default=1)
    background_passed = models.CharField(null=False, blank=False, choices=bg_choices, max_length=2)
    cv_resume = models.IntegerField(help_text="please enter a 4 digit year")
    masters = models.CharField(choices=masters_choices, max_length=3)
    CTL_notified = models.DateField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=50)
    city = models.CharField(null=False, blank=False, max_length=20)
    state = models.CharField(null=False, blank=False, max_length=2)
    zip = models.IntegerField(null=False, blank=False, help_text="please enter a 5 digit zipcode")
    primary_email = models.EmailField(null=False, blank=False)
    secondary_email = models.EmailField()
    primary_phone = PhoneField(null=False, blank=False)
    secondary_phone = PhoneField(null=True, blank=True)
    special_conditions_and_comments = models.TextField(null=True, blank=True)
    # semesters_taught = encrypt(models.TextField()) remove possibly
    archived = models.BooleanField()


class Classes(models.Model):
    adjunct_faculty_member = models.ForeignKey(AdjunctFacultyMember, on_delete=models.CASCADE)
    adj_class = models.CharField(max_length=10)
