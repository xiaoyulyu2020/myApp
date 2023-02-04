# base/ form.py
from django import forms
from django.forms import ModelForm
from .models import *


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
        labels = {            # bootstrap
            'patient': 'Patients',
            # bootstrap
            'employees': 'Employees [Hold Ctrl + Mouse select multiple employees]',
            # bootstrap
            'manager': 'Managers',
            'start': '',
            'end': '',
            'description': '',
        }
        widgets = {
            # bootstrap
            'employees': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Select Employees'}),
            'patient': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select A Patient'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select A Manager'}),
            'start': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Start At'}),
            'end': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'End At'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        labels = {            # bootstrap
            'name': '',
            # bootstrap
            'address': '',
            # bootstrap
            'phone': '',
            # bootstrap
            'email_address': '',
        }
        widgets = {
            # bootstrap
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            # bootstrap
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address'}),
            # bootstrap
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Contact Number'}),
            # bootstrap
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = MyEmployee
        fields = "__all__"
        labels = {            # bootstrap
            'first_name': '',
            # bootstrap
            'second_name': '',
            # bootstrap
            'email': '',
        }
        widgets = {
            # bootstrap
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            # bootstrap
            'second_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Second Name'}),
            # bootstrap
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
        }
