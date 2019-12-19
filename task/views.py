from django.shortcuts import render, HttpResponse, redirect
from task.models import Task
from django.contrib import messages


def home(request):
    return HttpResponse('Hay there')

def add(request):
    if request.method=="POST":
        task = request.POST.get('task','')
        
        task_obj = Task(task_name = task, status='incomplete')
        task_obj.save()
        messages.success(request, 'saved')

    return render(request, 'task/addTask.html')


def remove(request, id):
    task = Task.objects.filter(task_id = id)
    for i in task:
        i.delete()
        messages.info(request,"Task Deleted")
    return redirect('/')

def complete(request, id):
    print(id)
    task = Task.objects.filter(task_id = id)
    print(task)
    for i in task:
        i.status='completed'
        i.save()
        messages.info(request, "Status Updated")
    return redirect('/')