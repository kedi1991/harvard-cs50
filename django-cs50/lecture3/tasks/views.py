from django.shortcuts import render
from django import forms

from django.http import HttpResponseRedirect
from django.urls import reverse


#my form
class AddTaskForm(forms.Form):
    task = forms.CharField(label="Task name: ")
    priority = forms.IntegerField(label="Priority: ", max_value= 5)

# Create your views here.
def listtasks(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/listtasks.html", {"tasks": request.session["tasks"]})

def addtask(request):
   
    #request.post is the submitted data
    if (request.method == "POST"):
        form = AddTaskForm(request.POST)
        if (form.is_valid()):
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            #redirect to the list of tasks
            return HttpResponseRedirect(reverse("tasks:tasks"))
        else:
            return render(request, "tasks/addtask.html", {"form": form})

    return render(request, "tasks/addtaskfli.html", {"form": AddTaskForm()})