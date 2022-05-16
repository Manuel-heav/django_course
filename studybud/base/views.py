from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# To make a get request function here
# and this is the same as App.get
def home(request):
     return HttpResponse('Home page')

def room(request):
     return HttpResponse('Room')
