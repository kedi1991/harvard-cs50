from django.shortcuts import render

tasks = ["update uganda code", "update zambia code", "plan new stategy for africa"]
# Create your views here.
def listtasks(request):
    return render(request, "tasks/listtasks.html", {"tasks": tasks})