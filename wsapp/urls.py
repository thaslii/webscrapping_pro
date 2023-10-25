from django.contrib import admin
from django.urls import path
from wsapp import views

urlpatterns = [

    path('',views.home)
]
