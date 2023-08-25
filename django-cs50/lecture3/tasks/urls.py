from django.urls import path
from . import views

urlpatterns = [
    path('', views.listtasks, name="tasks")
]