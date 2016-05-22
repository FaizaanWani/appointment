# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone, dateparse

class FullName(models.Model):
    last_name = models.CharField('Surname', max_length=30)
    first_name = models.CharField('Name', max_length=20)
    middle_name = models.CharField('Middle Name', max_length=40)
    
    def __str__(self):
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)
    
    class Meta:
        abstract = True
        ordering = ['last_name']
        
class Specialization(models.Model):
    specialization = models.CharField('Specialty doctor', max_length=20)
    
    def __str__(self):
        return self.specialization
    
    class Meta:
        ordering = ['specialization']
    
class Patient(FullName):
    pass

class Doctor(FullName):
    specialization = models.ForeignKey(Specialization, verbose_name='specialization')
        
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, verbose_name='patient', blank=False)
    doctor = models.ForeignKey(Doctor, verbose_name='doctor', blank=False)
    date = models.DateField('physician acceptance date', blank=False, null=True)
    hour = models.TimeField('physician acceptance time', blank=False, null=True)
    TIME_CHOICES = (
        (dateparse.parse_time('09:00')),
        (dateparse.parse_time('10:00')),
        (dateparse.parse_time('11:00')),
        (dateparse.parse_time('12:00')),
        (dateparse.parse_time('13:00')),
        (dateparse.parse_time('14:00')),
        (dateparse.parse_time('15:00')),
        (dateparse.parse_time('16:00')),
        (dateparse.parse_time('17:00')),
    )
    
    def __str__(self):
        return "%s %s - %s" % (self.date, self.hour, self.doctor)

class Clinics(models.Model):
    """docstring for Clinics"""
    clinic_name = models.CharField('Name', max_length=120)
    clinic_loc = models.CharField('Location', max_length=120)
    clinic_time = models.CharField('Time', max_length=120)
    clinic_id = models.CharField('c_id', max_length=120)

    def __str__(self):
        return "%s %s %s" % (self.clinic_name, self.clinic_loc, self.clinic_time)


        