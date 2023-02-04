from django.contrib import admin
from .models import Patient, MyEmployee, Events

admin.site.register(MyEmployee)
admin.site.register(Events)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')
