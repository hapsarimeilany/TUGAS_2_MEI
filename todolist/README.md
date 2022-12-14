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
   
   
                                                         ----- README TUGAS 5 -----
   1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

   a. Inline CSS

      Inline CSS merupakan kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemennya memiliki atribut ```style``` yang merupakan tempat inline CSS ditulis.

   Kelebihan: Lebih membantu ketika ingin melakukan perubahan hanya pada satu elemen, proses permintaan HTTP lebih kecil dan proses load website akan lebih cepat.

    Kekurangan: Kurang efisien karena hanya bisa diterapkan pada satu elemen HTML.

   b. Internal CSS
   
   Internal CSS merupakan kode CSS yang ditulis dalam tag ```<style>``` dan kode HTML dituliskan di header (bagian atas).

   Kelebihan: Perubahan pada Internal CSS hanya berlaku pada satu halaman serta tidak perlu mengunggah beberapa file karena HTML dan CSS berada dalam satu file.

   Kekurangan: Tidak efisien jika ingin menggunakan CSS yang sama dalam beberapa file. 

   c. Eksternal CSS

      Eksternal CSS merupakan kode CSS yang ditulis secara terpisah dengan kode HTML Eksternal. CSS ditulis di sebuah file khusus yang berekstensi ```.css```. File eksternal CSS biasanya diletakkan setelah bagian ```<head>```pada halaman.

     Kelebihan: Ukuran file html menjadi lebih kecil dan struktur dari kode HTML lebih rapi, loading website lebih cepat, serta file css dapat digunakanuntuk lebih dari satu halaman website;.

   Kelemahan: Halaman akan menjadi berantakan saat file CSS gagal dipanggil oleh file HTML.
 
2. Jelaskan tag HTML5 yang kamu ketahui!

    - ```<!DOCTYPE>``` : untuk menentukan tipe dokumen
    - ```<html>```  : untuk membuat sebuah dokumen HTML
    - ```<title>``` : untuk membuat judul dari sebuah halaman
    - ```<body>``` : untuk membuat tubuh dari sebuah halaman
    - ```<h1> to <h6> ```: untuk membuat heading
    - ```<p>``` : untuk membuat paragraf
    - ```<br>``` : untuk memasukkan satu baris putus
    - ```<!--...-->``` : untuk membuat komentar
    - ```<html>``` : Tag untuk membuat dokumen HTML
    - ```<a>``` : untuk membuat hyperlink
    - ```<link>``` : untuk menghubungkan suatu dokumen dengan htmlnya
    - ```<table>``` : untuk membuat tabel
    - ```<th>``` : untuk membuat sebuah sel header tabel
    - ```<tr>``` : untuk membuat baris dalam sebuah tabel
    - ```<td>``` : untuk membuat sel dalam sebuah tabel
    - ```<style>``` : untuk membuat informasi style untuk dokumen
    - ```<div>```  : untuk membuat sebuah bagian dalam dokumen
    - ```<form>``` : untuk membuat form untuk meminta input dari user
    - ```<input>``` : untuk menunjukkan sebuah inputan berdasarkan tipe


3. Jelaskan tipe-tipe CSS selector yang kamu ketahui!
   
   - ID selector : cara menggunakan ID selector adalah dengan menambahkan beberapa ID pada tag html dan juga menambahkan ID selector pada file CSS maupun internal CSS dengan penulisan ```#namaID {...}```

    - Class selector : cara menggunakan class selector adalah dengan menambahkan beberapa class pada tag html dan juga menambahkan class selector pada file CSS maupun internal CSS dengan penulisan ```.namaClass {...}```

   - Element selector : cara menggunakan element selector adalah dengan memanfaatkan tag html sebagai selector untuk mengubah properti yang ada pada tag itu sendiri. Misalnya h1, p, h2, h3, dst. Contohnya ```h1{...}```
 

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!

   A. Halaman Login

      - Mengubah warna background halaman sesuai keinginan dengan menambahkan kode berikut di antara ```{% block meta %}``` dan ```{% endblock meta %}```

        ```
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background:  linear-gradient(to bottom,#c24eaf, #7982e6);
                height: 100vh;
            }
        </style>
        ```
      - Memposisikan semua element di halaman ```login.html``` di tengah menggunakan ```<div class = "login text-center">``` di bagian terluar ```{% block content %}```

      - Membungkus login table dalam ```card``` dengan menambahkan ```<div class="card p-3 mb-2 bg-ligth text-light shadow-lg p-3 mb-5 bg-body rounded position-absolute top-50 start-50 translate-middle" style="width: 25rem;">```

      - Memberi warna card tersebut di dalam block ```<style>``` dan mengatur warna-warna element di dalamnya

     - Mengubah tampilan button ```login``` menggunakan style ```btn-outline-light```

      B. Halaman Register

     - Memposisikan semua element di halaman ```register.html``` di tengah menggunakan ```<div class = "login text-center">``` di bagian terluar ```{% block content %}```
      
     - Membungkus register form dalam ```card``` yang mengandung text berwarna putih dengan menambahkan ```<div class="card p-3 mb-2 bg-ligth text-light shadow-lg p-3 mb-5 bg-body rounded position-absolute top-50 start-50 translate-middle" style="width: 40rem;">```

   C. Halaman Todolist

   - Membuat card untuk masing-masing task yang ada di dalam halaman todolist dengan menambahkan ```<div class="card p-3 mb-2 bg-ligth text-dark shadow-lg p-3 mb-5 bg-body rounded" style="width: 15rem; height: 15rem;">``` dan ```<div class="card-body">``` di dalam iterasi ```{% for item in todo_items %}```

   - Menambahkan ```<div class="row row-cols-1 row-cols-md-4 g-4">``` sebelum block iterasi ```{% for item in todo_items %}``` untuk mengatur baris dan kolom

   - Mengatur elemen-elemen di dalamnya (warna teks, button hapus dan update, jenis teks, dll)

   - Membuat ```navbar``` yang mengandung ```(username)'s Tasks```, ```login``` button, dan ```create task``` button serta mengatur warnanya di dalam block ```<style>```
    
     ```
     <nav class="navbar navbar-expand-lg bg-secondary">
        <div class="container-fluid">
           <div class="navbar-header">
               <style type="text/css">
                    .navbar {
                    background: #5f2c82;
                    background: -webkit-linear-gradient(to right, #6296b4ab, #624079);
                    background: linear-gradient(to right,  #6296b4ab, #624079);
                    }

                   .color-me {
                    color: whitesmoke;
                   }

               </style>
               <a class="navbar-brand text-white">
               <img src="https://img.icons8.com/external-soft-fill-juicy-fish/2x/external-task-business-management-soft-fill-soft-fill-juicy-fish-2.png" height="28" alt="" />
               <span class="color-me">{{nama}}'s Tasks</span> 
               </a>
               </div>

               <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                  <a class="btn btn-outline-light me-md-2" href="{% url 'todolist:buat-task' %}" role="button">?????? Create Task</a>
                  <a class="btn btn-outline-light" href="{% url 'todolist:logout' %}" role="button">Logout</a> 
             </div>      
         </div>
     </nav>
     ```

   D. Halaman Create Task

   - Memposisikan semua element di halaman ```create-task.html``` di tengah menggunakan ```<div class = "create-task text-center">``` di bagian terluar ```{% block content %}```

   - Membungkus create-task form dalam ```card``` yang mengandung text berwarna putih dengan menambahkan ```<div class="card p-3 mb-2 bg-ligth text-light shadow-lg p-3 mb-5 bg-body rounded position-absolute top-50 start-50 translate-middle" style="width: 40rem; height: 15rem;">``` dan ```<div class="card-body">``` serta mengatur warna card di dalam block ```<style>```
               


       
        

