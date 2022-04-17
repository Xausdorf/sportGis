from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def welcome(request):
    return render(request, 'main/welcome.html')

def map(request):
    return render(request, 'main/map.html')

def info(request):
    return render(request, 'main/info.html')
