from venv import create
from django.urls import path
from todolist.views import create_task, show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='buat-task'),
]
