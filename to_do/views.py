from django.shortcuts import HttpResponse, render
from task.models import Task

def home(request):
    task = Task.objects.all()
    contex = {
        'tasks':task,
    }
    return render(request, 'home/home.html', contex)
