from django.contrib import admin

# Register your models here.
from .models import Registration

# admin.site.register(Registration)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'token', 'fullname', 'department', 'department_other', 'degree', 'degree_other', 'hostel', 'year', 'other_year', 'contact', 'email', 'linkedin', 'city', 'country', 'dept_mentees', 'designation', 'company_name', 'work_profile', 'pref', 'field_other', 'mentees', 'preference_no_preference', 'preference_final_year_undergrad', 'preference_other_undergrad', 'preference_mtech_students', 'preference_phd_students', 'buddy', 'isNew']




class NewRegistrationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'isNew']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(isNew=True)
    
admin.site.register(Registration, RegistrationAdmin)

