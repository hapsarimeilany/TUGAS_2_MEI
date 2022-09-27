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


# Create your views here.
#@login_required(login_url='/todolist/login/')

def show_todolist(request):
    # todo_items = [
    #     {
    #         "date": "27 Sept 2022",
    #         "title": "Todo1",
    #         "description": "Todolist pertama"
    #     },
    #     {
    #         "date": "27 Sept 2022",
    #         "title": "Todo 2",
    #         "description": "Todolist kedua"
    #     }
    # ]

    todo_items = Task.objects.all()

    data = {
        'todo_items': todo_items,
        'nama': 'Meilany',
        'NPM' : '2106751436'
    }

    return render(request, "todolist.html", data)

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

def saveform(request):
    form = CreateTaskForm(request.POST)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HTTPResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')