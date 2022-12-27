from django.shortcuts import render, HttpResponse
from. models import employe,test
from.forms import empForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializer import itemserializ

from rest_framework.views import APIView
# Create your views here.

global multikey


# @api_view(['GET'])
# def home(request,pk):
#     t1=employe.objects.all()
#     t2=employe.objects.get(id=1)

#     ser=itemserializ(t2)

#     return Response(ser.data)

@api_view(['GET'])
def call(request,pk):
    ta=employe.objects.all()
    print(ta)
    task=ta.get(id=pk)
    
    print(task)
    re=itemserializ(task,many=True)
    
    return Response(re.data)



def test(request):

    
    
    form=empForm()
    task1=None
    
    if request.method=='POST':
        id1=request.POST['emp_id']
        print(id1)
        
        task1=employe.objects.filter(emp_id=id1)[0].id
        
        multikey=task1
        print(multikey)
        
    
    contex={
                'form':form,
                'task':task1
            }
            
    return render(request,'test.html',contex)



# @api_view(['GET'])
def test1(request):
   
    
    print(multikey)
    
   
    return HttpResponse("hellpo")
    



