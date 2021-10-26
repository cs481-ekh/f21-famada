from datetime import datetime
import re

from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator
from django.forms.widgets import SelectDateWidget
from phone_field import PhoneField
from django_cryptography.fields import encrypt
from django import forms


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
    DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
           '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
           '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
           '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
           '2012', '2013', '2014', '2015')

    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be entered in the format: 1112223333"
    )

    a_f_eaf_c_crs_list = models.CharField(null=False, blank=False, choices=a_f_eaf_c_crs_choices, max_length=3)
    semester = models.CharField(max_length=4, help_text="Please enter in format: semester year (ex: FA19)")
    first_name = models.CharField(null=False, blank=False, max_length=30)
    last_name = models.CharField(null=False, blank=False, max_length=30)
    date_of_birth = models.DateField(null=False, blank=False, default=datetime.now)
    employeeID = models.IntegerField(null=False, blank=False, unique=True, primary_key=True)
    step_rate = models.CharField(null=False, blank=False, choices=sr_choices, max_length=10, default='step 1')
    I9_completed = models.DateField(null=False, blank=False, help_text="Please enter a date.")
    I9_greater_than_3_years = models.IntegerField(null=False, blank=False, help_text="Please enter a number of years.")
    background_passed = models.CharField(null=False, blank=False, choices=bg_choices, max_length=2)
    cv_resume = models.IntegerField(help_text="please enter a year")
    masters = models.CharField(choices=masters_choices, max_length=3)
    CTL_notified = models.DateField(null=False, blank=False, help_text="Please enter a date.")
    address = models.CharField(null=False, blank=False, max_length=50)
    city = models.CharField(null=False, blank=False, max_length=20)
    state = models.CharField(null=False, blank=False, max_length=2)
    zip = models.IntegerField(null=False, blank=False, )
    primary_email = models.EmailField(null=False, blank=False)
    secondary_email = models.EmailField()
    primary_phone = models.CharField(null=False, blank=False, max_length=12, validators=[phone_regex])
    secondary_phone = models.CharField(validators=[phone_regex], max_length=12)
    special_conditions_and_comments = models.TextField(blank=True)
    archived = models.BooleanField()


class Classes(models.Model):
    adjunct_faculty_member = models.ForeignKey(AdjunctFacultyMember, on_delete=models.CASCADE)
    adj_class = models.CharField(max_length=10)
