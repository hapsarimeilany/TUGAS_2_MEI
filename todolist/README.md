1. Apa kegunaan {% csrf_token %} pada elemen <form> ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

   {% csrf_token %} berguna untuk mencegah serangan CSRF yang akan membuat penyerang tersebut tidak mungkin melakukan HTTP request yang secara sepenuhnya valid yang cocok untuk diumpankan ke user yang menjadi korban. Apabila {% csrf_token %} tidak ada, maka ketika request selanjutnya dibuat, aplikasi di bagian sisi server akan menolak request tersebut karena akan berbahaya bagi form tersebut. Oleh karena itu {% csrf_token %} sangatlah penting untuk keamanan form. 

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual!

   Ya, kita bisa membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) yaitu dengan cara sebagai berikut:
   1) Membuat file ```forms.py```. Contohnya sebagai berikut
      ```
      class Input_Form(forms.ModelForm):
            class Meta:
                  model = Person
                  fields = ['display_name']
            error_messages = {
                  'required' : 'Please Type'
            }
            input_attrs = {
                  'type' : 'text',
                  'placeholder' : 'Nama Kamu'
            }
            display_name = forms.CharField(label='', required=False, 
            max_length=27, widget=forms.TextInput(attrs=input_attrs))
       ```
   2) Mengimport ```form.py``` ke ```views.py```. Contohnya:
      ```
      from .forms import Input_Form

      def formulir(request):
             response = {'input_form' : Input_Form}
             return render(request, 'index.html', response)
      ```
   3) Merge bagian HTML dari ```form.py``` di HTML template. Contohnya: 
      ```
      <form action="savename" method="POST">
           {% csrf_token %}
         Name: {{input_form.as_p}}
         <input type="submit" value="Submit">
      </form>
      ```
   4) Validate POST argument berdasarkan ```form.py```
      ```
      def savename(request):
          form = Input_Form(request.POST or None)
          if (form.is_valid and request.method == 'POST'):
             form.save()
             return HttpResponseRedirect('/')
          else:
              return HttpResponseRedirect('/')
      ```

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

   1) Alur data berawal dari user yang memasukkan alamat http://host/path kemudian browser akan men-generate HTTP request ke alamat tersebut
   2) Kemudian server akan menerima HTTP request tersebut dan menentukan views.py yang mana yang akan dihandle oleh path.
   3) Setelah berhasil menentukan views.py yang akan digunakan untuk menghandle path, server akan men-generate halaman HTML form menuju browser.
   4) Browser akan menampilkan layout HTML form yang telah digenerate kepada user sehingga user dapat melihat form tersebut dan mengisinya.
   5) Setelah form diisi, browser akan men-generate HTTP request, method, dan arguments ke URL destination berdasarkan halaman HTML form. 
   6) Server kembali menerima HTTP request dan kembali menentukan views.py yang mana yang akan menghandle path. 
   7) Server men-generate HTML page yang berisi data-data yang telah disimpan dan kemudian ditampilkan kepada user melalui browser.


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

    4) Pada ```urls.py``` di folder ```todolist``` tambahkan 
      
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

   E. Membuat Form Create Task

   1) Membuat fungsi ```create_task``` yang menerima parameter request. Isinya sebagai berikut:
      ```
      def create_task(request):
         if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            tambah_todolist = Task(user=request.user, title=title, 
            description=description, date=datetime.datetime.now())
            tambah_todolist.save()
            return redirect('todolist:show_todolist')
      return render(request, 'create-task.html')
      ```
   2) Membuat ```create-task.html``` pada folder ```templates``` yang berada di dalam folder ```todolist``` dengan isi sebagai berikut:
      ```
      {% extends 'base.html' %}

      {% block content %}  

      <div class = "create-task">
         <h3>Let's Create Your New Task!</h3>
         <form action="" method="POST">
             {% csrf_token %}
             <div>
                 <label for="title">Task: </label>
                 <input id="title" type="text" name="title" placeholder="Write your task here" required>
             </div>

             <p></p>
             <div>
                 <label for="description">Description: </label>
                 <input id="description" type="text" name="description" placeholder="Describe your task here" required>
             </div>

             <p></p>
             <input type="submit" value="Tambahkan Task Baru">
        </form>
        </div>
        {% endblock content %}
        ```
     3) Membuat tombol ```create task``` dengan menambahkan potongan kode berikut pada ```todolist.html``` yang diletakkan setelah end tag table ```</table>``` dan sebelum ```{% endblock content %}```
        ```
        <button><a href="{% url 'todolist:buat-task' %}">Create Task</a></button>
        ```
    4) Menambahkan path create-task pada ```urls.py``` di dalam folder ```todolist```
       ```
       ...
       path('create-task/', create_task, name='buat-task'),
       ...
       ```
   
   F. Mengimplementasi Tugas Bonus (Update)

   1) Menambahkan model di dalam ``class Task``` pada ```models.py``` dari aplikasi ```todolist```
      ```
      is_finished = models.BooleanField(default=False)
      ```
   2) Membuat fungsi ```updateStatusTask``` pada ```views.py``` dengan parameter ```request``` dan ```i``` sebagai berikut:
      ```
      def updateStatusTask(request, i):
          updated_task = Task.objects.get(id=i)
          updated_task.is_finished = not updated_task.is_finished
          updated_task.save()
          return redirect("todolist:show_todolist")
      ```
    3) Menambahkan table header di dalam ```todolist.html```
       ```
       ...
       <th>Button Update</th>
       ...
       ```
    4) Menambahkan data cell untuk is_finished dan menambahkan update button di dalam iterasi ```todo_items``` pada ```todolist.html```
       ```
       {% for item in todo_items %}
            <tr>
                ...
                <td>{{item.is_finished}}</td> 
                <td><button class="btn-ans"><a href="{% url 'todolist:updateStatusTask' item.id %}">Update</a></td>
            </tr>
       {% endfor %}
       ```
    5) Menambahkan path update pada ```urlpatterns``` di ```urls.py```
       ```
       ...
       path("update/<int:i>/", updateStatusTask, name="updateStatusTask")
       ...
       ```
   G. Mengimplementasi Tugas Bonus (Delete)

   1) Membuat fungsi ```deleteTodo``` dengan parameter ```request``` dan ```i``` pada ```views.py```
      ```
      def deleteTodo(request, i):
         deleted_task = Task.objects.get(id=i)
         deleted_task.delete()
         return redirect("todolist:show_todolist")
      ```
   2) Menambahkan table header di dalam ```todolist.html```
       ```
       ...
       <th>Delete Task</th>
       ...
       ```
    3) Menambahkan data cell berisi ```delete``` button di dalam iterasi ```todo_items``` pada ```todolist.html```
       ```
       {% for item in todo_items %}
            <tr>
                ...
                <td><button class="btn-ans"><a href="{% url 'todolist:deleteTodo' item.id %}">Delete</a></button></td>
            </tr>
       {% endfor %}
       ```
    4) Menambahkan path delete pada ```urlpatterns``` di ```urls.py```
       ```
       ...
       path('deleteTodo/<int:i>', deleteTodo, name='deleteTodo'),
       ...
       ```
       
      
LINK APLIKASI TODOLIST HEROKU: http://mei-watchlist.herokuapp.com/todolist/login/?next=/todolist/ 

   AKUN 1: meilanyhpsr (password: sukasuka)

   AKUN 2: meilaaa (password: sukasuka)
