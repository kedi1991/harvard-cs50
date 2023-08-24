from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('family/', views.family, name="family"),
    path('<str:name>', views.greeting, name="greeting")
]
