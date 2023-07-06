from django.contrib import admin

# Register your models here.
from .models import Registration

# admin.site.register(Registration)

# class RegistrationAdmin(admin.ModelAdmin):
#     list_display = ['token', 'fullname', 'isNew']


class NewRegistrations(admin.ModelAdmin):
    list_display = ['token', 'fullname', 'isNew']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(isNew=True)
    
admin.site.register(Registration, NewRegistrations)

