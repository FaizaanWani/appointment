from django.contrib import admin

from .models import *
    
class AppointmentInline(admin.TabularInline):
    model = Appointment
    fields = ['date', 'hour', 'patient']
    extra = 1

class DoctorAdmin(admin.ModelAdmin):
    inlines = [AppointmentInline]
    list_display = ('__str__', 'specialization')
    list_filter = ['specialization']

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialization)
