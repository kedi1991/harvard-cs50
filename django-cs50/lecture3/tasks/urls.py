from django.urls import path
from . import views

urlpatterns = [
    path('index', views.listtasks, name="tasks"),
    path("add", views.addtask, name="addtask"),
]