from django.shortcuts import render
from .models import Room

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, "home.html", context)

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    return render(request,"room.html")

def navbar(request):
    return render(request,"navbar.html")
