from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path('index', views.listtasks, name="tasks"),
    path("add", views.addtask, name="addtask"),
]