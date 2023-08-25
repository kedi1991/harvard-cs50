from django.shortcuts import render

# Create your views here.
def listtasks(request):
    return render(request, "tasks/listtasks.html")