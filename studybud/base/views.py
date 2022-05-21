from django.shortcuts import render
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
          print(request.POST)
     context = {'form': form}
     return render(request,'base/room_form.html', context)
