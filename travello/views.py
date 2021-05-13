from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User,auth




# Create your views here.


def index(request):
    
    dests= Destination.objects.all()


    return render(request, "index.html" ,{'dests':dests})
def about(request):
    return render(request,'about.html' )

def contact(request):
    return render(request,'contact.html' )




