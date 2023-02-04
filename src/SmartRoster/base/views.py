# base / views.py

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from calendar import HTMLCalendar
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages


# Pass data
def home(request):
    return render(request, 'home.html', {})

# =============== Event ===================


def eventList(request):
    form = Events.objects.all()
    context = {'form': form}
    return render(request, "event_list.html", context)


def eventAdd(request):
    submit = False
    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/event_add?submit=True')
    else:
        form = EventsForm
        if "submit" in request.GET:
            submit = True
            messages.success(request, ("Add Event Successful."))

        context = {'form': form, 'submit': submit}
        return render(request, "event_add.html", context)


def eventUpdate(request, eventId):
    event = Events.objects.get(pk=eventId)
    form = EventsForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('eventList')

    return render(request, 'event_update.html', {'event': event, 'form': form})


def eventDelete(request, eventId):
    event = Events.objects.get(pk=eventId)
    event.delete()
    return redirect('eventList')
# ============== end Event=============


# ============== patient ==============
def patientAdd(request):
    submit = False
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patient_add?submit=True')
    else:
        form = PatientForm
        if "submit" in request.GET:
            submit = True
            messages.success(request, ("Registration successful."))

        context = {'form': form, 'submit': submit}
        return render(request, "patient_add.html", context)


def patientList(request):
    form = Patient.objects.all()
    context = {'form': form}
    return render(request, "patient_list.html", context)


def searchPatient(request):
    if request.method == "POST":
        search = request.POST['search']
        patient = Patient.objects.filter(name__contains=search)
        context = {'search': search, 'patient': patient}
        return render(request, 'search_patient.html', context)
    else:
        return render(request, 'search_patient.html', {})


def patientUpdate(request, patientId):
    patient = Patient.objects.get(pk=patientId)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patientList')
    context = {'patient': patient, 'form': form}
    return render(request, 'event_update.html', context)


def patientDelete(request, patientId):
    patient = Patient.objects.get(pk=patientId)
    patient.delete()
    return redirect('patientList')
# ============== end Patient ==================

# ============== Employee ===================


def employeeList(request):
    form = MyEmployee.objects.all()
    context = {'form': form}
    return render(request, "employee_list.html", context)


def employeeAdd(request):
    submit = False
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employee_add?submit=True')
    else:
        form = EmployeeForm
        if "submit" in request.GET:
            submit = True
            messages.success(request, ("Registration successful."))

        context = {'form': form, 'submit': submit}
        return render(request, "employee_add.html", context)


def employeeDelete(request, employeeId):
    employee = MyEmployee.objects.get(pk=employeeId)
    employee.delete()
    return redirect('employee_list')


def employeeUpdate(request, employeeId):
    employee = MyEmployee.objects.get(pk=employeeId)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    context = {'employee': employee, 'form': form}
    return render(request, 'employee_update.html', context)


# ============== end Employee ==================

# =================calendar ref to https://stackoverflow.com/questions/39902405/fullcalendar-in-django=====================


def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }
    return render(request, 'caltable.html', context)


def all_events(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            # 'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            # 'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    return JsonResponse(out, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    form = EventsForm()
    form.save()
    data = {form}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
# end of calendar
