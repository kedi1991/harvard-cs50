from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello jayden")

def family(request):
    return HttpResponse("Family of 3 people")

def greeting(request, name):
    return HttpResponse(f"Hello  {name}")