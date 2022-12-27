from django.shortcuts import render,redirect,HttpResponse
from .models import Task
from.forms import TaskForm,updateForm
# Create your views here.

def index(request):
    
    tasks=Task.objects.all()
    print(tasks)
    frm=TaskForm()
    if request.method=='POST':
        frm=TaskForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('/')
    
    tasks=Task.objects.all()
    form={
        'tasks':tasks,
        'for':frm,
    }
    return render (request,'list.html',form)

def updatetask(request,pk):
    task=Task.objects.get(id=pk)
    print(task)
    form=updateForm(instance=task)
    if request.method=='POST':
        
        form1=updateForm(request.POST,instance=task)
        if form1.is_valid():
            form1.save()
            redirect('/')
    contex= {'form':form}
    return render(request,'update_task.html',contex)

def confirm(pk):
    task=Task.objects.get(id=pk)
    task.delete()

def delete(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':

        task.delete()
        return redirect('list')

    return render(request,'delete.html')