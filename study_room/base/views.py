from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Room,Topic
from .forms import RoomForm
from django.contrib.auth.models import User

from django.db.models import Q
# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    topics = Topic.objects.all()

    if q:
        rooms = Room.objects.filter(
            Q(topic__name__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q)
        )
    else:
        rooms = Room.objects.all()
    
    room_count=rooms.count()

    context = {'rooms': rooms, 'topics': topics,'room_count':room_count}
    return render(request, "home.html", context)



def room(request,pk):
    rooms = Room.objects.get(id=pk)
    return render(request,"room.html")

def navbar(request):
    return render(request,"navbar.html")

def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

            
  
    context={'form' : form}
    return render(request,"base/room_form.html",context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')
    context = {}
    return render(request,'base/login_register.html',context)