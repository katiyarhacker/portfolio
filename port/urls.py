from django.shortcuts import render
from django.http import HttpResponse
from . import views
from django.urls import path
 # or from port import views

urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('weatherapp/', views.weatherapp, name='weatherapp'),
    path('todo_List/', views.todo_List, name='todo_List'),  # Example
]
