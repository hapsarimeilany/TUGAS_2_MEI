1. Perbedaan antara JSON, XML, dan HTML!
   
   JSON (JavaScript Object Notation) merupakan format pertukaran data yang jauh lebih mudah bagi komputer dalam proses penguraian data yang sedang dikirim. JSON didesain menjadi self-describing sehingga JSON sangat mudah untuk dimengerti. JSON mendukung penggunaan array dan pembuatan object. Sintax pada JSON yang merupakan turunan dari Object JavaScript juga terhitung pendek. Format JSON berupa text yang datanya disimpan dalam bentuk pasangan key dan value.

   Sedangkan XML (Extensible Markup Language) merupakan bahasa markup (bukan bahasa pemrograman) dan bagian dari setiap aplikasi web yang didesain self-descriptive sehingga dengan membaca XML tersebut kita dapat memahami informasi yang disampaikan oleh data tertulis. XML tidak mendukung penggunaan array seperti pada JSON. Tag yang digunakan pada XML dibuat secara manual oleh programmer. Bentuk dokumen XML yaitu berupa struktur tree yang dimulai dari root, branch, sampai berakhir pada leaves.

   Sama seperti XML dan berbeda dengan JSON, HTML merupakan bahasa markup karena tidak dapat memberikan fungsi dinamis yang digunakan untuk membuat dan menyusun halaman serta aplikasi web. Sebagian besar elemen bahasa markup ini memiliki tag pembuka dan penutup yang menggunakan syntax <tag></tag>.

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   
   Data delivery merupakan suatu proses pengiriman data dari satu stack ke stack lainnya yang dilakukan dalam proses pembangunan suatu platform. Data delivery perlu dilakukan agar data dapat ditampilkan sesuai dengan permintaan client. Format data delivery yang akan digunakan menyesuaikan dengan permintaan client yaitu dapat berupa format xml, json, maupun html.
   
3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!

   A. Membuat Aplikasi Django beserta Konfigurasi Modelnya

      Karena pada tugas 3 ini kita menggunakan proyek yang dibuat pada tugas 2 pekan lalu, maka kita tidak perlu membuat repositori baru di akun GitHub. Yang pertama kali dilakukan yaitu langsung membuat aplikasi Django beserta konfigurasi modelnya sebagai berikut:
   
      1. Membuat sebuah ```Django-app``` bernama ```mywatchlist``` dengan perintah ```python manage.py startapp mywatchlist``` .
      2. Menambahkan aplikasi ```mywatchlist``` ke dalam variabel ```INSTALLED_APPS``` yang ada di dalam ```settings.py``` di folder ```project_django``` untuk mendaftarkan django-app yang sudah dibuat.

         ```bash
            INSTALLED_APPS = [
            ...,
            ‘mywatchlist’,
            ]
         ``` 
      3. Menambahkan potongan kode berikut pada file ```models.py``` yang ada di folder ```mywatchlist``` untuk membentuk skema model.

         ```python
            from django.db import models
            
            class WatchList(models.Model):
                title = models.CharField(max_length=50)
                watched = models.CharField(max_length=50)
                rating = models.IntegerField()
                release_date = models.TextField()
                review = models.TextField()
         ```
     4. Mempersiapkan migrasi skema model ke dalam datasbase Django lokal dengan perintah ```python manage.py makemigrations``` .
     5. Menerapkan skema model yang telah dibuat ke dalam database Django lokal dengan perintah ```python manage.py migrate``` .
     6. Membuat folder bernama ```fixtures``` di dalam aplikasi ```mywatchlist ``` dan mengisinya dengan berkas bernama ```initial_watchlist_data.json``` yang berisi kode yang akan menampilkan data-data watchlist saya.
     7. Menjalankan perintah ```python manage.py loaddata initial_watchlist_data.json``` untuk memasukkan data tersebut ke dalam database Django lokal.

   B. Implementasi Views Dasar
        
      1. Membuat sebuah fungsi yang menerima parameter ```request``` dan mengembalikan ```render(request, “mywatchlist.htm”)``` di dalam ```views.py``` yang ada pada folder m ```watchlist```.
         ```bash
            def show_mywatchlist(request):
                return render(request, "mywatchlist.html")
         ```
      2. Membuat sebuah folder bernama ```templates``` di dalam folder aplikasi ```mywatchlist``` dan membuat berkas bernama ```mywatchlist.html```. Isinya sebagai berikut:
         ```python
            {% extends 'base.html' %}

            {% block content %}

            <h1>Tugas 3 PBP</h1>
            <h4>Nama: </h4>
            <p>Fill me!</p>
            <h4>Student ID: </h4>
            <p>Fill me!</p>

            <body>
            <h2 style="text-align:center;">{{pesan}}</h2>
            </body>

            <table>
               <thead>
                  <tr>
                      <th>Title</th>
                      <th>Watched</th>
                      <th>Rating</th>
                      <th>Release Date</th>
                      <th>Review</th>
                  </tr>
               </thead>
               
               {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
               {% for film in list_film %}
               <tr>
                  <th>{{film.title}}</th>
                  <th>{{film.watched}}</th>
                  <th>{{film.rating}}</th>
                  <th>{{film.release_date}}</th>
                  <th>{{film.review}}</th>
               </tr>
               {% endfor %}
            </table>

            {% endblock content %}

         ```
      3. Membuat sebuah berkas bernama ```urls.py``` di dalam folder aplikasi ```mywatchlist``` untuk melakukan routing terhadap fungsi views yang telah dibuat agar HTML dapat menampilkannya di browser.

          ```python
           from django.urls import path
           from mywatchlist.views import show_mywatchlist
            
           app_name = 'mywatchlist'
       
           urlpatterns = [
           path('', show_mywatchlist, name='show_mywatchlist'),
          ```
    4. Mendaftarkan aplikasi ```mywatchlist``` ke dalam ```urls.py``` yang ada pada folder ```project_django``` dengan kode berikut pada variable ```urlpatterns```.
          ```bash
             ...
             path('mywatchlist/', include('mywatchlist.urls')),
             ...
          ```
    5. Menjalankan proyek Django dengan perintah ```python manage.py runserver``` dan membuka 
```http://localhost:8000/mywatchlist/``` untuk mengecek keberhasilan proses routing sebuah fungsi views yang dapat menampilkan data-data ke html.

   C. Menghubungkan Models dengan Views dan Template
       
      1. Import models yang sudah dibuat ke dalam ```views.py``` untuk melakukan pengambilan data dari database.

         ```bash
            from django.shortcuts import render
            from mywatchlist.models import WatchList
         ```
     2. Menambahkan potongan kode yang berfungsi untuk memanggil fungsi query ke model database ke dalam fungsi ```show_mywatchlist``` serta menambahkan ```context``` ke dalam parameter return render agar data yang ada dalam ```context``` turut dirender ke dalam halaman HTML.

        ```python
           context = {
           'list_film': data_film_watchlist,
           'nama': 'Meilany',
           'NPM': '2106751436',
           }
           return render(request, "mywatchlist.html", context)
        ```
      Dilanjutkan dengan proses mapping terhadap data yang telah ikut di-render pada fungsi views untuk dapat memunculkannya di halaman HTML.

      1. Membuka file HTML yang sudah dibuat sebelumnya pada folder ```templates``` yang ada di dalam direktori ```wishlist```.
      2. Ubah ```Fill me!``` yang ada di dalam HTML tag <p> menjadi ```{{nama}}``` dan  membuat ```{{NPM}}``` untuk menampilkan nama dan npm saya di halaman HTML. Contohnya adalah sebagai berikut:

         ```bash
            <h4>Nama: </h4>
            <p>{{nama}}</p>
            <h4>Student ID: </h4>
            <p>{{NPM}}</p>
         ```
      3. Melakukan iterasi terhadap variabel ```list_film``` yang telah dirender ke dalam HTML.
         ```bash
            {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
            {% for film in list_film %}
            <tr>
                <th>{{film.title}}</th>
                <th>{{film.watched}}</th>
                <th>{{film.rating}}</th>
                <th>{{film.release_date}}</th>
                <th>{{film.review}}</th>
            </tr>
            {% endfor %}
         ```
      4. Melakukan pengecekan apakah data yang ikut dimasukkan ke dalam views ikut muncul di dalam halaman web.

    D. Mengembalikan Data dalam Bentuk XML dan JSON

      1. Membuka ```views.py``` yang ada pada folder ```wishlist``` dan buatlah sebuah fungsi yang menerima parameter request. Selanjutnya tambahkan import ```HttpResponse``` dan ```Serializer``` pada bagian paling atas

         ```python
            from django.shortcuts import render
            from mywatchlist.models import WatchList
            from django.http import HttpResponse
            from django.core import serializers

            def show_mywatchlist(request):
                data_film_watchlist = WatchList.objects.all()
         ```
      2. Membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada WatchList
         ```bash
            data = BarangWishlist.objects.all()
         ```
      3. Tambahkan return function berupa ```HttpResponse``` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan XML
         ```python
          def show_xml(request):
              data = WatchList.objects.all()
              return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

         def show_json(request):
              data = WatchList.objects.all()
              return HttpResponse(serializers.serialize("json", data), content_type="application/json")
         ```
     4. Buka ```urls.py``` yang ada pada folder ```wishlist``` dan import fungsi yang sudah kamu buat tadi.
        ```bash
           from mywatchlist.views import show_mywatchlist
           from mywatchlist.views import show_xml
           from mywatchlist.views import show_json
        ```
     5. Tambahkan path url ke dalam ```urlpatterns``` untuk mengakses fungsi yang sudah diimpor tadi.

        ```python
          from django.urls import path
          from mywatchlist.views import show_mywatchlist
          from mywatchlist.views import show_xml
          from mywatchlist.views import show_json 
          from mywatchlist.views import show_json_by_id
          from mywatchlist.views import show_xml_by_id

          app_name = 'mywatchlist'

          urlpatterns = [
               path('', show_mywatchlist, name='show_mywatchlist'),
               path('xml/', show_xml, name='show_xml'),
               path('json/', show_json, name='show_json'),
               path('html/', show_mywatchlist, name='show_mywatchlist'),
               path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
               path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
          ]
        ```

   E. Pembuatan Pesan Bonus
      
      1. Membuat conditional di dalam fungsi ```show_mywatchlist``` dan menambahkan variabel pesan untuk menampilkan pesan berdasarkan banyak jumlah watched maupun not watched.

     2. Memanggil pesan yang akan ditampilkan ke dalam mywatchlist.html dan mengaturnya agar posisinya berada di tengah
        ```bash
           <body>
           <h2 style="text-align:center;">{{pesan}}</h2>
           </body>
        ```
     3. Menambahkan ````path('html/', show_mywatchlist, name='show_mywatchlist')```` pada urls.py untuk membentuk link html mywatchlist.

   F. Mengisi unit testing pada testing?

      Membuat kode yang mampu digunakan untuk mengetes tugas MPPI ini terutama watchlist/json/html/xml.


   G. Mendeploy Aplikasi Django ke Heroku

     
      1. Membuat app baru ```mywatchlist``` di heroku dengan nama ```mei-watchlist```.
      2. Salin API Key dari akun. API Key dapat ditemukan di Account Settings -> API 
      3. Membuka konfigurasi repositori GitHub dan bukalah bagian Secrets untuk GitHub ```Actions (Settings -> Secrets -> Actions)```.
      4. Tambahkan variabel repository secret baru untuk melakukan deployment. Pasangan Name-Value dari variabel yang akan dibuat dapat diambil dari informasi yang dicatat pada file teks sebelumnya. Contohnya adalah sebagai berikut.
         ```bash
           (NAME)HEROKU_APP_NAME
           (VALUE)APLIKASI-SAYA
      5. Simpan variabel-variabel tersebut.

      6. Bukalah tab GitHub ```Actions``` dan jalankan kembali workflow yang gagal. 
      
      POSTMAN http://localhost:8000/mywatchlist/html/
      
      ![image](https://user-images.githubusercontent.com/112571938/191585550-8ce6a81b-e3f2-4247-9bb6-ad3954887e11.png)
      ![image](https://user-images.githubusercontent.com/112571938/191585944-be5003b2-e2f7-4197-ae7e-f5679a243384.png)
      ![image](https://user-images.githubusercontent.com/112571938/191586028-530a56a3-0ded-4b99-bb79-ff3beb9e90b2.png)
      ![image](https://user-images.githubusercontent.com/112571938/191586131-2ceab9e8-e547-426b-b656-48b1db969938.png)
      ![image](https://user-images.githubusercontent.com/112571938/191586205-9e756aa0-80e4-47c4-b345-6331258a871b.png)
      ![image](https://user-images.githubusercontent.com/112571938/191586290-f2275baf-a3a8-4c6b-9d6d-3a7afad4c3af.png)
      ![image](https://user-images.githubusercontent.com/112571938/191586374-26d05087-ffe7-4787-9a53-d297c14a5102.png)
      ![image](https://user-images.githubusercontent.com/112571938/191586480-6a4f52ca-79a6-4326-8593-cf3fe3ec5dec.png)
      ![image](https://user-images.githubusercontent.com/112571938/191586588-55c2586c-b055-4423-bfee-9f49a109aac7.png)
      
      
     POSTMAN http://localhost:8000/mywatchlist/json/
     
     ![image](https://user-images.githubusercontent.com/112571938/191586893-73fcddcc-ff91-4147-8104-579c2fb33094.png)
     ![image](https://user-images.githubusercontent.com/112571938/191586984-6271f0f0-b52c-4cf2-ba33-92bad0ab0a17.png)
     ![image](https://user-images.githubusercontent.com/112571938/191587056-a08810b8-6481-4cd6-9770-4241866f3ea6.png)
     ![image](https://user-images.githubusercontent.com/112571938/191587127-6d08812d-b13d-4221-b4d8-94acce3301d4.png)
     ![image](https://user-images.githubusercontent.com/112571938/191587199-17b82781-3e63-40bc-945a-8347a82f80b2.png)
     ![image](https://user-images.githubusercontent.com/112571938/191587282-d1863c0d-65d0-4f20-9939-074be8e89b30.png)
     ![image](https://user-images.githubusercontent.com/112571938/191587397-ffaca5ab-6f58-4a69-b254-391f96750dc1.png)
     ![image](https://user-images.githubusercontent.com/112571938/191587459-737f3d5a-c3e3-4c47-ae60-0e50f02b162b.png)


    POSTMAN http://localhost:8000/mywatchlist/xml/
    
    ![image](https://user-images.githubusercontent.com/112571938/191587609-a6e78ab2-ea3d-4810-9cdd-bc7cff07847a.png)
    ![image](https://user-images.githubusercontent.com/112571938/191587667-b7f210d5-8a8f-400f-b554-3170351fb498.png)
    ![image](https://user-images.githubusercontent.com/112571938/191587710-931fbce0-7268-44a3-95c4-9ee4a5791168.png)
    ![image](https://user-images.githubusercontent.com/112571938/191587767-32af67e6-5989-4996-a175-7a79db841a0a.png)
    ![image](https://user-images.githubusercontent.com/112571938/191587884-b1ae43f8-3a31-465a-abbb-7a5a6da32f4d.png)
    ![image](https://user-images.githubusercontent.com/112571938/191587938-a78c1aca-63d4-463e-baa9-4cac792b828a.png)






















