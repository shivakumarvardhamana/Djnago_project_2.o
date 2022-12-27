from django.urls import path,include
from . import views

urlpatterns=[
    # path('',views.home),
    # path('add/',views.itemadd),
    path('deatail/',views.deatail,name="deatail"),
    path('create/',views.create,name='create'),
    path('update/<str:pk>/',views.update,name="update"),
    path('delete/<str:pk>/',views.delete,name='delete'),
]