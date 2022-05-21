from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.

# rooms = [
#      {'id': 1, 'name': 'Lets learn python'},
#      {'id': 2, 'name': 'Lets learn design'},
#      {'id': 3, 'name': 'Lets learn sup'},
# ]
# To make a get request function here
# and this is the same as App.get
def home(request):
     rooms = Room.objects.all()
     return render(request, 'base/home.html',{'rooms': rooms})

def room(request,pk):
     room = Room.objects.get(id=pk)
     context = {'room': room}
     return render(request, 'base/room.html', context)


def createRoom(request):
     form = RoomForm()

     if request.method == 'POST':
          form = RoomForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')
     context = {'form': form}
     return render(request,'base/room_form.html', context)


def updateRoom(request,pk):
     room = Room.objects.get(id=pk)
     form = RoomForm(instance = room)

     if request.method == 'POST':
          form = RoomForm(request.POST, instance = room)
          if form.is_valid():
               form.save()
               return redirect('home')

     context = {'form': form}
     return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
     room  = Room.objects.get(id=pk)
     if request.method == 'POST':
          room.delete()
          return redirect('home')
     return render(request, 'base/delete.html', {'obj': room})
