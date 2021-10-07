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
    bg_choices = {  #background choices
        ('P', 'pass'),
        ('NA', 'NA'),
        (' ', ' '),
        ('--', '--')
    }
    a_f_eaf_c_crs_list = encrypt(models.CharField(null=False, blank=False, choices=a_f_eaf_c_crs_choices, max_length=3))
    semester = encrypt(models.CharField(default='--', max_length=4))
    first_name = encrypt(models.CharField(null=False, blank=False, max_length=30))
    last_name = encrypt(models.CharField(null=False, blank=False, max_length=30))
    date_of_birth = encrypt(models.DateField(null=False, blank=False))
    employeeID = encrypt(models.IntegerField(null=False, blank=False, unique=True))
    step_rate_dept = encrypt(models.CharField(null=False, blank=False, max_length=10))
    I9_completed = encrypt(models.DateField(null=False, blank=False, default='NA'))
    I9_greater_than_3_years = encrypt(models.IntegerField(null=False, blank=False, default='NA'))
    background_passed = encrypt(models.CharField(null=False, blank=False, default='NA', choices=bg_choices, max_length=2))
    cv_resume = encrypt(models.CharField(default='NA', max_length=4))
    masters = encrypt(models.CharField(default='NA', max_length=30))
    CTL_notified = encrypt(models.DateField(null=False, blank=False, default='NA'))
    classes = encrypt(models.TextField(null=False, blank=False, ))
    address = encrypt(models.CharField(null=False, blank=False, max_length=50))
    city = encrypt(models.CharField(null=False, blank=False, max_length=20))
    state = encrypt(models.CharField(null=False, blank=False, max_length=2))
    zip = encrypt(models.IntegerField(null=False, blank=False, ))
    primary_email = encrypt(models.EmailField(null=False, blank=False))
    secondary_email = encrypt(models.EmailField(default="johnDoe@gmail.com"))
    primary_phone = encrypt(PhoneField(null=False, blank=False,  help_text='Primary phone number'))
    secondary_phone = encrypt(PhoneField(default='000-000-0000', blank=True, help_text='Secondary phone number'))
    special_conditions_and_comments = encrypt(models.TextField())
    semesters_taught = encrypt(models.TextField())
    archive = encrypt(models.BooleanField())

