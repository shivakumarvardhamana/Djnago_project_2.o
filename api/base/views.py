from django.shortcuts import render,redirect


from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import item
from .serializers import itemserializ

from . serializers import itemserializ
# @api_view(['GET'])
# def home(request):

#     items=item.objects.all()
#     #serialize=itemserializ(items,many=True)

#     serialize=itemserializ(items,many=True)

   
#     return Response(serialize.data)

# @api_view(['POST'])
# def itemadd(request):

#     serializ=itemserializ(data=request.data)
#     if serializ.is_valid():
#         serializ.save()


#     return Response(serializ.data)


@api_view(['GET'])

def deatail(request):
    task=item.objects.all()
    ser=itemserializ(task,many=True)

    return Response(ser.data)


@api_view(['POST'])
def create(request):
    task=item.objects.all()

    ser=itemserializ(data=request.data)

    if ser.is_valid():
        ser.save()

    return Response(ser.data)


@api_view(['POST'])

def update(request,pk):
    task=item.objects.get(id=pk)
    ser=itemserializ(instance=task,data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['DELETE'])

def delete(request,pk):
    task=item.objects.get(id=pk)
    task.delete()

    return redirect('deatail')