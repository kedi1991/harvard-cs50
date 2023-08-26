from django.shortcuts import render
from django import forms

tasks = ["update uganda code", "update zambia code", "plan new stategy for africa"]

#my form
class AddTaskForm(forms.Form):
    task = forms.CharField(label="Task name: ")
    priority = forms.IntegerField(label="Priority: ", max_value= 5)

# Create your views here.
def listtasks(request):
    return render(request, "tasks/listtasks.html", {"tasks": tasks})

def addtask(request):
    return render(request, "tasks/addtask.html", {"form": AddTaskForm()})