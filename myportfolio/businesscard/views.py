from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    # return HttpResponse('<h1 text-align: center>HELLO THERE</h1>')
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')