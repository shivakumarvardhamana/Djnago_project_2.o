from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
from .forms import userform,usercreateform,AuthenticationForm

from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):
    form=userform
    if request.method=="POST":
        form=userform(request.POST)
        print("checkinfg")
        if form.is_valid():
            print("saved")
            form.save()
    print("not saved")
    contex={'form':form}
    return render(request,'home.html',contex)


def userreg(request):

    form=usercreateform

    if request.method=="POST":
        print("went into save")
        form=usercreateform(request.POST)
        if form.is_valid:
            print("saved")
            form.save()
    print("not saving")
    contex={'form':form}

    return render(request,'user.html',contex)


def login1(request):
    form = AuthenticationForm()
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('user',username)

        print('pass',password)
        user1 = authenticate(username=username, password=password)
        print('authenticat',user1)
        if user1 is not None:
            login(request,user1)
            messages.info(request,'login successfully')
            print("logined success fully")
            return redirect('userreg')
        else:
        
            messages.error(request,'bad credentials')
            return redirect('home')
    contex={'form':form}
    return render(request,'login.html',contex)
