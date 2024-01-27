from django.shortcuts import render,redirect
from .models import TodoModel

# Create your views here.
def todoview(request):
    mytodo= TodoModel.objects.all()
    context={'mytodos':mytodo}
    return render (request,"todopages/homepage.html",context)

def addtask(request):
    #code to add data to the database
    mytask=request.POST['task']
    TodoModel(task=mytask).save()
    return redirect(request.META['HTTP_REFERER'])

def deletetask(request,taskpk):
    #code to delete data from the database
    TodoModel.objects.filter(id=taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])

def edittaskview(request,taskpk):
    #code to update data from the database
    context={'todopk':taskpk}
    return render(request,"todopages/edittask.html",context)

def edittask(request,taskpk):
    userenteredtask=request.POST['task']
    todo=TodoModel.objects.filter(id=taskpk)[0]
    todo.task=userenteredtask
    todo.save()
    return redirect('homepage')
