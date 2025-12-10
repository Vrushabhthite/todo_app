from django.shortcuts import render
from todo_gem_app.models import Task


def home(request):
    task=Task.objects.filter(is_completed=False)
    # print(task)
    context={
        'task':task,
    }
    return render(request,'home.html',context)