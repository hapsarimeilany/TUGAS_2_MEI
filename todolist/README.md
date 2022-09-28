
1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
   
   A. Membuat Aplikasi Todolist
   1) Membuat aplikasi todolist dengan menjalankan perintah ```python manage.py startapp todolist```

    2) Mendaftarkan aplikasi ```todolist``` ke dalam proyek Django yaitu dengan menambahkan kode di bawah ke dalam ```setting.py``` di folder ```project_django```
       ``` 
       INSTALLED_APPS = [
       ...,
       'todolist',
       ]

   3) Mengisi kode berikut pada ```models.py``` di folder ```todolist```:
      ```
      from django.db import models

      class Task(models.Model):
           user = models.ForeignKey(User, on_delete=models.CASCADE,)
           date = models.DateField()
           title = models.TextField()
           description = models.TextField()

   4) Menjalankan perintah ```python manage.py makemigrations``` dan ```python manage.py migrate``` untuk menyiapkan dan menerapkan skema model yang telah dibuat ke dalam database Django lokal.


   B. Menambahkan Path Todolist sehingga Pengguna Dapat Mengakses http://localhost:8000/todolist
    
      1) Membuat path todolist pada ```urls.py``` yang ada di folder aplikasi ```todolist``` sebagai berikut:
        
           ```
           urlpatterns = [
           path('', show_todolist, name='show_todolist'),
           ]
           ```
      2) Membuat fungsi ```show_todolist``` di ```views.py``` pada folder ```todolist``` yang akan menampilkan data pada halaman todolist, sebagai berikut:

          ```
          def show_todolist(request):
              todo_items = Task.objects.filter(user=request.user)
              user = request.user

              data = {
              'todo_items': todo_items,
              'nama': user
              }
              return render(request, "todolist.html", data)
         ```
           
   C.  Mengimplementasikan Form Registrasi
       
      1) Tambahkan import berikut pada ```views.py``` di folder ```todolist```:
 
           ```
           from django.shortcuts import redirect
           from django.contrib.auth.forms import UserCreationForm
           from django.contrib import messages
           ```

      2) Membuat fungsi bernama ```register``` dengan parameter ```request``` pada ```views.py``` di folder ```todolist``` yang berisi:

         ```
         def register(request)         
             form = UserCreationForm()

             if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                   form.save()
                   messages.success(request, 'Akun telah berhasil dibuat!')
                   return redirect('todolist:login')
    
             context = {'form':form}
             return render(request, 'register.html', context)
         ```
       
     3) Membuat berkas HTML baru dengan nama ```register.html``` pada folder ```templates``` di dalam folder ```todolist``` yang berisi:

        ```
        {% extends 'base.html' %}

        {% block meta %}
        <title>Registrasi Akun</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
    
            <h1>Formulir Registrasi</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                       </tr>  
                   </table>  
              </form>

            {% if messages %}  
            <ul>   
                {% for message in messages %}  
                   <li>{{ message }}</li>  
                   {% endfor %}  
            </ul>   
         {% endif %}

        </div>  

        {% endblock content %}
        ```

    4) Pada ```urls.py``` di folder ```todolist, tambahkan 
      
       ```
       from wishlist.views import register
       ```
    5) Tambahkan path register ke ```urlpattern``` di ```urls.py```
       ```
       ...
       path('register/', register, name='register'),
       ....
       
   D. Mengimplementasi Form Login

    1) Membuat fungsi ```login_user``` di ```views.py``` pada folder ```todolist``` yang seperti berikut:
       ```
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
       ```
    2) Tambahkan import ```authenticate``` dan ```login``` pada bagian paling atas
       ```
       from django.contrib.auth import authenticate, login
       ```
    3) Membuat berkas ```login.html``` pada folder ```templates``` aplikasi ```todolist```
    
    4) Import fungsi ```login_user``` di ke dalam ```urls.py``` pada folder ```todolist```
       ```
       from todolist.views import login_user
       ```
    5) Tambahkan path url login ke dalam ```urlpatterns``` untuk mengakses fungsi yang sudah diimpor tadi
       ```
       ...
       path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
       ...
       ```
