import datetime
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect 
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')

def show_todolist(request):
    todo_items = Task.objects.filter(user=request.user)
    user = request.user

    data = {
        'todo_items': todo_items,
        'nama': user
    }
    return render(request, "todolist.html", data)

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tambah_todolist = Task(user=request.user, title=title, description=description, date=datetime.datetime.now())
        tambah_todolist.save()
        return redirect('todolist:show_todolist')
    return render(request, 'create-task.html')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def deleteTodo(request, taskId):
    deleted_task = Task.objects.get(id=taskId)
    deleted_task.delete()
    return redirect("todolist:show_todolist")

def updateStatusTask(request, taskId):
    updated_task = Task.objects.get(id=taskId)
    updated_task.is_finished = not updated_task.is_finished
    updated_task.save()
    return redirect("todolist:show_todolist")

def get_todolist_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def create_task_modal(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        new_todolist = Task(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.now()
        )
        new_todolist.save()
        return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')
