# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
import datetime
from django import forms
from .models import *
# from django.utils import timezone,dateparse
from datetimewidget.widgets import DateWidget
from config.clinic import CLINICS

today = "%s" % timezone.now().date()
end_date = "%s" % (timezone.now().date()+datetime.timedelta(days=90))

date_options = {
                'weekStart': '1',
                'startDate': today,
                'endDate': end_date,
                'daysOfWeekDisabled':'"0,6"'
               }
class AppointmentForm(forms.Form):
    # print Specialization.objects.all()
    specialization = forms.ModelChoiceField(label='specialization', 
                                            queryset=Specialization.objects.all(), 
                                            widget=forms.Select(attrs={'class':'form-control',
                                                                       'onChange':'submit()',}))
    # print specialization,type(specialization)
    doctor = forms.ModelChoiceField(label='doctor', 
                                    queryset=Doctor.objects.all(), 
                                    widget=forms.Select(attrs={'class':'form-control',
                                                              'onChange':'submit()',}))
    clinics = forms.ModelChoiceField(label='clinics', 
                                    queryset=Clinics.objects.all())
    print  Clinics.objects.all(),clinics,">>>>"                                                            
    date = forms.DateField(label='Date of receipt', 
                           widget=DateWidget(options = date_options, 
                           usel10n=True, 
                           bootstrap_version=3),
                           initial=timezone.now().date)
                                                
    hour = forms.ChoiceField(label='Time of receipt', 
                             choices=[(x, x) for x in Appointment.TIME_CHOICES],
                             widget=forms.Select(attrs={'class':'form-control'}))
    
    last_name = forms.CharField(label='Surname', 
                                max_length=30,
                                widget=forms.TextInput(attrs={'class':'form-control'}))
                                                          
    first_name = forms.CharField(label='Name', 
                                 max_length=20,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    
    middle_name = forms.CharField(label='middle name', 
                                  max_length=40,
                                  widget=forms.TextInput(attrs={'class':'form-control'}))
    

    def __init__(self, *args, **kwargs):
        spec_id = kwargs.pop('spec_id', False)
        doc_id = kwargs.pop('doc_id', False)
        doc_id = False if doc_id == '' else doc_id
        spec_id = False if spec_id == '' else spec_id
        date = kwargs.pop('date', False)
        hour = kwargs.pop('hour', False)
        
        super(AppointmentForm, self).__init__(*args, **kwargs)
        
        if spec_id != False and doc_id == False:
          self.fields['doctor'].queryset=Doctor.objects.filter(specialization_id=spec_id)
        
        if doc_id != False and spec_id == False:
            self.fields['specialization'].empty_label = Doctor.objects.get(id=doc_id).specialization
            
        if date != False:
            booked_hours =[x[0] for x in Appointment.objects.filter(doctor_id=doc_id, date__contains=date).values_list('hour')]
            f = filter(lambda x: x not in booked_hours, Appointment.TIME_CHOICES)
            self.fields['hour'].choices = [(x,x) for x in f ]
