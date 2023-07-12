from django.contrib import admin

# Register your models here.
from .models import Registration
from .views import export

# admin.site.register(Registration)

# class RegistrationAdmin(admin.ModelAdmin):
#     list_display = ['token', 'fullname', 'isNew']


class NewRegistrations(admin.ModelAdmin):
    list_display = ['token', 'fullname', 'isNew']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(isNew=True)
    
    actions = ['export_data']

    def export_data(self, request, queryset):
        response = export(request)
        return response

    # export_data.short_description = 'Export Selected Registrations'
    
admin.site.register(Registration, NewRegistrations)

