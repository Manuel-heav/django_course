from django.shortcuts import render

# Create your views here.


# To make a get request function here
# and this is the same as App.get
def home(request):
     return render(request, 'home.html')

def room(request):
     return render(request, 'room.html')

