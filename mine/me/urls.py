from django.contrib import admin
from django.urls import path 
from . import views


urlpatterns = [
    
    path('',views.home,name=""),
    path('user/',views.userreg,name="userreg"),
    path('login/',views.login1,name="login1"),
]