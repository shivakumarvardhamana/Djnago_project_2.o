from django.urls import path
from . import views
urlpatterns=[
    
    
    path('test/',views.test,name='test'),
    path('call/<str:pk>/',views.call,name='call'),
    path('test1/',views.test1,name='test1'),
]