from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello jayden")

def family(request):
    #return HttpResponse("Family of 3 people")
    return render(request, "hello/family.htm")

def greeting(request, name):
    #return HttpResponse(f"Hello  {name}")
    return render(request, "hello/greet.htm", {"name": name})