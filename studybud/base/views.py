from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse("Home page!")

# def room(request):
#     return HttpResponse("ROOM")

rooms = [
    {'id': 1, 'name': "let's learn"},
    {'id': 2, 'name': "How to get data"},
    {'id': 3, 'name': "From the views"},
]


def home(request):
    return render(request, 'home.html', {'rooms' : rooms})

def room(request):
    return render(request, "room.html")