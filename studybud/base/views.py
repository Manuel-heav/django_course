from django.shortcuts import render

# Create your views here.

rooms = [
     {'id': 1, 'name': 'Lets learn python'},
     {'id': 2, 'name': 'Lets learn design'},
     {'id': 3, 'name': 'Lets learn sup'},
]
# To make a get request function here
# and this is the same as App.get
def home(request):
     return render(request, 'home.html',{'rooms': rooms})

def room(request):
     return render(request, 'room.html')

