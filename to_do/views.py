from django.shortcuts import HttpResponse, render, redirect
from task.models import Task


def home(request):
    task = Task.objects.all()
    contex = {
        'tasks':task,
    }
    return render(request, 'home/home.html', contex)

def query(request):
    qry = request.GET.get('query','')
    tasks = Task.objects.all()
    taskList = [(i.task_name, i.task_id) for i in tasks]
    data = {
        "query":qry,
        'tasks' : []
    }
    for i,j in taskList:
        if qry in i:  data['tasks'].append(Task.objects.get(task_id =j))  

    return render(request, 'home/search.html', data)