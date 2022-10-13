1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming!
 
   Pada asynchronus programming, pengguna bisa tetap berinteraksi dengan pagenya sambil menunggu respons dari server yang masih me-load data. Contohnya adalah website W3Schools. Sebaliknya, synchronus programming menerapkan click-wait-reresh sehingga user harus menunggu proses load data dari server dan baru bisa berinteraksi dengan pagenya lagi setelah server memberikan responsenya. Contohnya adalah server SIAK-NG yang mana user baru bisa war hanya ketika ia berhasil masuk ke servernya.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini!

   Paradigma event-driven programming merupakan pemrograman yang alur programnya dijalankan berdasarkan kejadian suatu event/peristiwa sebagai pemicunya. Pada tugas kali ini, contoh dari penerapan event-driven programming adalah penggunaan button create-task. Saat button tersebut diklik oleh user, maka program akan menampilkan modal untuk tambah task baru sebagai responsenya.

3. Jelaskan penerapan asynchronous programming pada AJAX!

      Asynchronus programming pada AJAX membuat usernya tidak perlu melakukan click-wait-refresh. AJAX adalah teknik untuk membuat web app lebih interaktif lagi dengan meng-update suatu page secara dinamis sehingga usernya tidak perlu reload page secara keseluruhan jika ada suatu perubahan kecil.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

   A. Mengimplementasikan GET AJAX
      
      - Membuat view baru yang mengembalikan data task dalam bentuk json

        ```
        def get_todolist_json(request):
            data = Task.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize('json', data), content_type='application/json')
        ```

      - Membuat ```/todolist/json``` yang mengarah ke view baru
        ```
        urlpatterns = [
             ...
             path('json/', get_todolist_json, name='get_todolist_json'),
        ]
        ```

     - Mengambil data task dengan menggunakan AJAX di dalam block ```<script>``` di ```todolist.html``` (line 100-137)
       
   B. Mengimplementasikan POST AJAX

      - Membuat view baru bernama ```create_task_modal``` untuk menambahkan task baru ke dalam database
        ```
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
        ```

     - Membuat ```modal``` di ```todolist.html``` yang berisi form untuk membuat ```task baru``` (line 66-95)

     - Membuat handler untuk button ```Create Task``` di dalam block ```<script>``` di ```todolist.html``` yang memicu munculnya ```modal```
       ```
       $('.create-task').click( function() {
         $('.modal').toggle();
       });
       ```

     - Membuat handler untuk button close ```X``` di dalam block ```<script>``` di ```todolist.html``` yang memicu munculnya ```modal```
       ```
       $('.btn-close').click( function() {
         $('.modal').toggle();
       });
       ```

    - Implementasi POST AJAX untuk mengirimkan isi form ```Create Task``` ke card task yang akan dimunculkan di halaman ```show_todolist``` setelah button ```Create``` diklik
      ```
      $('.btn-save').click(function() {

        // Get values dari elemen di halamanan form:
        let title = $('.title').val();
        let description = $('.description').val();
        let CSRFtoken =$('input[name="csrfmiddlewaretoken"]').val();
        
        
        // Kirim data yang diperoleh dengan POST
        $.post( '/todolist/add/', {title: title, description: description, csrfmiddlewaretoken: CSRFtoken});
      ```

       Load data dengan menggunakan kode yang sama dengan implementasi GET AJAX untuk menampilkan card task baru (line 162-201).
