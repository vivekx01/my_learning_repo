from django.shortcuts import render, redirect
from .models import CounterModel

# Create your views here.

def helloworld(request):
    name='Vivek'
    obj= CounterModel.objects.filter(id=1)[0]
    ournumber=obj.number
    context={'name':name,'number':ournumber}
    return render (request,"helloworld/helloworld.html",context)

def increment(request):
    #code to increment the number
    obj= CounterModel.objects.filter(id=1)[0]
    obj.number=int(obj.number)+1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def decrement(request):
    #code to decrement the number
    obj= CounterModel.objects.filter(id=1)[0]
    obj.number=int(obj.number)-1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    #code to reset value to 0
    obj= CounterModel.objects.filter(id=1)[0]
    obj.number=0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])