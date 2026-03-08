from django.shortcuts import render
from todo_gem_app.models import Task



def home(request):
    task=Task.objects.filter(is_completed=False)
    complete_task=Task.objects.filter(is_completed=True)
    # print(complete)
    # print(task)
    context={
        'task':task,
        'complete_task':complete_task,
        
    }
    return render(request,'home.html',context)

