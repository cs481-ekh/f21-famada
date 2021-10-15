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
        ('P', 'pass'),
        ('NA', 'NA'),
        ('F', 'fail')
    }
    sr_choices = {  # step rate choices
        ('1', 'step 1'),
        ('2', 'step 2'),
        ('3', 'step 3'),
        ('F', 'faculty')
    }
    a_f_eaf_c_crs_list = encrypt(models.CharField(null=False, blank=False, choices=a_f_eaf_c_crs_choices, max_length=3))
    semester = encrypt(models.CharField(default='--', max_length=4))
    first_name = encrypt(models.CharField(null=False, blank=False, max_length=30))
    last_name = encrypt(models.CharField(null=False, blank=False, max_length=30))
    date_of_birth = encrypt(models.DateField(null=False, blank=False))
    employeeID = encrypt(models.IntegerField(null=False, blank=False, unique=True))
    step_rate = encrypt(models.CharField(default="NA", null=False, blank=False, choices=sr_choices, max_length=10))
    I9_completed = encrypt(models.DateField(null=False, blank=False, default='NA'))
    I9_greater_than_3_years = encrypt(models.IntegerField(null=False, blank=False, default='NA'))
    background_passed = encrypt(
        models.CharField(null=False, blank=False, choices=bg_choices, max_length=2))
    cv_resume = encrypt(models.IntegerField(default='NA', help_text="please enter a year"))
    masters = encrypt(models.CharField(choices=masters_choices, max_length=3))
    CTL_notified = encrypt(models.DateField(null=False, blank=False, default='NA'))
    classes = encrypt(models.TextField(null=False, blank=False, ))
    address = encrypt(models.CharField(null=False, blank=False, max_length=50))
    city = encrypt(models.CharField(null=False, blank=False, max_length=20))
    state = encrypt(models.CharField(null=False, blank=False, max_length=2))
    zip = encrypt(models.IntegerField(null=False, blank=False, ))
    primary_email = encrypt(models.EmailField(null=False, blank=False))
    secondary_email = encrypt(models.EmailField(default="NA"))
    primary_phone = encrypt(PhoneField(null=False, blank=False, help_text='Primary phone number'))
    secondary_phone = encrypt(PhoneField(default='NA', blank=True, help_text='Secondary phone number'))
    special_conditions_and_comments = encrypt(models.TextField())
    # semesters_taught = encrypt(models.TextField()) remove possible
    archived = encrypt(models.BooleanField(default=False))


class Classes(models.Model):
    class_name = encrypt(models.CharField(max_length=10, help_text="Chem"))
    class_number = encrypt(models.CharField(max_length=10, help_text="101"))
