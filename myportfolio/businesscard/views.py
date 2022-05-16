from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    # return HttpResponse('<h1 text-align: center>HELLO THERE</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')