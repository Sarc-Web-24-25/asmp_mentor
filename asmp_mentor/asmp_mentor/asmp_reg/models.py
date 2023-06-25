from django.db import models
from .options import *


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    department = models.CharField(
        max_length=255, choices=BRANCH_CHOICES, default='default_value'
    )
    department_other = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, choices=DEGREE_CHOICES)
    degree_other = models.CharField(max_length=255, blank=True, null=True)
    hostel = models.CharField(
        max_length=255, choices=HOSTEL_CHOICES, default='default_value'
    )
    year = models.CharField(max_length=255, choices=YEAR_CHOICES, null=True)
    other_year = models.CharField(
        max_length=255, blank=True, null=True, default='Your Default Value'
    )
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255, default='default_value')
    city = models.CharField(max_length=255, default='Your Default Value')
    country = models.CharField(
        max_length=100, default='Your Default Value', choices=COUNTRY_CHOICES
    )
    dept_mentees = models.CharField(
        max_length=255, choices=DEPT_MENTEES_FIELDS, default='Your Default Value'
    )
    designation = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    work_profile = models.CharField(max_length=255, null=True)
    pref = models.CharField(
        max_length=255, choices=FIELDS, default='default_value'
    )
    field_other = models.CharField(max_length=255, blank=True, null=True)
    mentees = models.CharField(
        max_length=255, choices=MENTEES, default='Your Default Value'
    )
    preference_no_preference = models.BooleanField(default=False)
    preference_final_year_undergrad = models.BooleanField(default=False)
    preference_other_undergrad = models.BooleanField(default=False)
    preference_mtech_students = models.BooleanField(default=False)
    preference_phd_students = models.BooleanField(default=False)
    availability = models.CharField(
        max_length=255, default='Your Default Value'
    )
    buddy = models.CharField(
        max_length=255, default='Your Default Value'
    )

    def __str__(self):
        return self.fullname

