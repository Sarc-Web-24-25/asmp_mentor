# from django.db import models

# # Create your models here.

# from django.db import models
# from .options import *

# class Registration(models.Model):

#     id = models.AutoField(primary_key=True)
#     fullname = models.CharField(max_length=255)
#     rollno = models.CharField(max_length=9)
#     department = models.CharField(max_length=255, choices=BRANCH_CHOICES)
#     department_other = models.CharField(max_length=255, blank=True, null=True)
#     degree = models.CharField(max_length=255, choices=DEGREE_CHOICES)
#     degree_other = models.CharField(max_length=255, blank=True, null=True)
#     # graduation_year=models.CharField( max_length=10)
#     graduation_year = models.IntegerField()
#     experience = models.TextField()
#     contact = models.CharField(max_length=12)
#     email = models.CharField(max_length=255)

#     placementOrGrad = models.CharField(max_length=255, choices=OPTIONS)

#     designation = models.CharField(max_length=255, blank=True)
#     company_name = models.CharField(max_length=255, blank=True)
#     experience = models.TextField()

#     field_pref1 = models.CharField(
#         max_length=255, choices=PLACEMENT_FIELDS, null=True)
#     field_pref2 = models.CharField(
#         max_length=255, choices=PLACEMENT_FIELDS, null=True)
#     field_pref3 = models.CharField(
#         max_length=255, choices=PLACEMENT_FIELDS, null=True)

#     university_name = models.CharField(max_length=255, blank=True, null=True)

#     branch = models.CharField(
#         max_length=255, choices=BRANCH_CHOICES, null=True)
#     branch_subdivision = models.CharField(
#         max_length=255, blank=True, null=True)

#     preferred_mentees = models.IntegerField(null=True)

#     suggestions = models.TextField(blank=True, null=True)

#     alumni_recommendations = models.TextField(blank=True, null=True)
#     def __str__(self):
#         return self.fullname+"_"+self.field_pref1

from django.db import models
from .options import *

class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    department = models.CharField(max_length=255, choices=BRANCH_CHOICES)
    department_other = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, choices=DEGREE_CHOICES)
    degree_other = models.CharField(max_length=255, blank=True, null=True)
    hostel = models.CharField(max_length=255, choices=HOSTEL_CHOICES)
    year = models.CharField(max_length=255, choices=YEAR_CHOICES)
    other_year = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255) 
    city = models.CharField(max_length=255, default='Your Default Value')
    country = models.CharField(max_length=100, default='Your Default Value', choices=COUNTRY_CHOICES)
    dept_mentees = models.CharField(
        max_length=255, choices=YEAR_CHOICES, default='Your Default Value')
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    work_profile = models.CharField(max_length=255)
    pref = models.CharField(max_length=255, choices=PLACEMENT_FIELDS)
    mentees = models.CharField(max_length=255, choices=MENTEES)
    dept_mentees = models.CharField(max_length=255)
    suggestions = models.CharField(max_length=255)
    availability = models.CharField(
        max_length=255, default='Your Default Value')


    




