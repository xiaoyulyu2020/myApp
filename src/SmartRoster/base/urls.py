# base / urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('caltable/', views.calendar, name="caltable"),
    path('eventList/', views.eventList, name="eventList"),
    path('patientList/', views.patientList, name="patientList"),
    path('patient_add/', views.patientAdd, name="patient_add"),
    path('patient_update/<patientId>',
         views.patientUpdate, name='patient_update'),
    path('patient_delete/<patientId>',
         views.patientDelete, name="patient_delete"),
    path('search_patient/', views.searchPatient, name="search_patient"),
    path('event_add/', views.eventAdd, name="event_add"),
    path('event_update/<eventId>', views.eventUpdate, name="event_update"),
    path('event_delete/<eventId>',
         views.eventDelete, name="event_delete"),
    path('employee_add/', views.employeeAdd, name="employee_add"),
    path('employee_update/<employeeId>',
         views.employeeUpdate, name="employee_update"),
    path('employee_delete<employeeId>',
         views.employeeDelete, name="employee_delete"),
    path('employee_list/', views.employeeList, name="employee_list"),
]
