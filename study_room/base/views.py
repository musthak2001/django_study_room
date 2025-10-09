from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from .models import Room, Topic
from .forms import RoomForm

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
    
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, "home.html", context)



def room(request, pk):
    room = get_object_or_404(Room, id=pk)
    return render(request, "room.html", {'room': room})



def navbar(request):
    return render(request, "navbar.html")



@login_required(login_url='login')
def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            messages.success(request, 'Room created successfully!')
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_form.html", context)



@login_required(login_url='login')
def updateRoom(request, pk):
    room = get_object_or_404(Room, id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here !!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully!')
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = get_object_or_404(Room, id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here !!')

    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted successfully!')
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'base/login_register.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')