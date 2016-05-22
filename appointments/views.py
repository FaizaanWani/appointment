# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from .models import *
from .forms import *

def index(request):
    if request.method == 'POST':
        print request.method
        spec = request.POST.get('specialization', False)
        doc = request.POST.get('doctor', False)
        date = request.POST.get('date', False)
        hour = request.POST.get('hour', False)
        ln = request.POST.get('last_name')
        fn = request.POST.get('first_name')
        mn = request.POST.get('middle_name')
        form = AppointmentForm(request.POST, spec_id=spec, doc_id=doc, date=date, hour=hour)
        print ln,fn,mn, hour
        if len(ln) > 0  and len(fn) > 0 and len(mn) > 0:
            p, created = Patient.objects.get_or_create(last_name=ln, first_name=fn, middle_name=mn)
            appointment = Appointment(patient_id=p.id, doctor_id=doc, date=date, hour=hour)
            try:
                p.full_clean() and appointment.full_clean()
                created and appointment.save()
                return HttpResponseRedirect(reverse('success', args=()))
            except ValidationError as e:
                print(e)
                
        return render(request, 'appointments/index3.html', {'form': form})
    else:
        form = AppointmentForm()
        # print form
        return render(request, 'appointments/index3.html', {'form': form})
        
def success(request):
    return HttpResponse("You have successfully written to the doctor")
