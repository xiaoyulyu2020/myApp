from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse("Home page!")

# def room(request):
#     return HttpResponse("ROOM")

rooms = [
    {'id': 1, 'name': "let's learn << room 1 >>"},
    {'id': 2, 'name': "How to get data << room 2 >>"},
    {'id': 3, 'name': "From the views << room 3 >> "},
]

# Pass data
def home(request):
    context = {"rooms":rooms}
    return render(request, 'home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room_Html' : room}
    return render(request, "room.html", context)