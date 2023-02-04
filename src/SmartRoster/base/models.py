from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Patient(models.Model):
    name = models.CharField('Patient Name', max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField('Phone Number', max_length=30)
    email_address = models.EmailField('Patient Email', blank=True)

    def __str__(self):
        return self.name


class MyEmployee(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.EmailField('Employee Email')

    def __str__(self):
        return self.first_name + " " + self.second_name


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Event Name', max_length=30)
    patient = models.ForeignKey(
        Patient, blank=True, null=True, on_delete=models.SET_NULL)
    employees = models.ManyToManyField(MyEmployee, blank=True)
    manager = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)

    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Scheduling'
        verbose_name_plural = 'Scheduling'

    def __str__(self):
        return self.name
