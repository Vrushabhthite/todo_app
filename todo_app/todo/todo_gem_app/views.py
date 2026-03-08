from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def addTask(request):
     if request.method=='POST':
          task=request.POST.get('task','').strip()
          if task=='':
               messages.error(request,'Task cannot be empty!')
               # print("task cannot be empty")
               return redirect('home')
          Task.objects.create(task=task)
          return redirect('home')

def mark_as_done(request,pk):
     task=get_object_or_404(Task,pk=pk)
     #task=Task.objects.get(id=pk)
     task.is_completed=True
     task.save()
     return redirect('home')



def mark_as_undone(request,pk):
     task=get_object_or_404(Task,pk=pk)
     task.is_completed=False
     task.save()
     return redirect('home')


def delet_task(request,pk):
     task=get_object_or_404(Task,pk=pk)
     task.delete()
     return redirect('home')


def edit_task(request,pk):
     get_task=get_object_or_404(Task,pk=pk)
     if request.method=="POST":
          new_task=request.POST['task']
          get_task.task=new_task
          get_task.save()
          return redirect('home')
     else:
          context={
               'get_task':get_task,
          }
          return render(request,'edit.html',context)
   


# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

#         if password1 != password2:
#             messages.error(request, "Passwords do not match")
#             return redirect('register')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#             return redirect('register')

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password1
#         )
#         user.save()
#         messages.success(request, "Registration successful")
#         return redirect('login')

#     return render(request, 'register.html')




# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, "Invalid username or password")
#             return redirect('login')

#     return render(request, 'register.html')



# def logout_view(request):
#     logout(request)
#     return redirect('login')