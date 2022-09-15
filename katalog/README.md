1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

    ![Client Request Bagan](https://github.com/hapsarimeilany/TUGAS_2_MEI/blob/main/katalog/RequestClientBagan.png)

    Pada urls.py terjadi proses mapping untuk mengarahkan request dari HTTP ke tampilan(view) yang sesuai berdasarkan pemetaan URL tersebut. Selain itu, URL mapper dapat melakukan pencocokan pola string atau angka tertentu yang muncul di URL kemudian meneruskannya ke fungsi view yang ada pada views.py sebagai data. 

    views.py mengandung fungsi pengendali permintaan. Ia menerima permintaan dan mengembalikan respon HTTP. views.py akan mengakses data-data yang diperlukannya untuk memenuhi permintaan melalui model yang ada pada models.py kemudian mendelegasikan formatting respons ke dalam berkas html. models.py merupakan obyek python yang mendefinisikan struktur data aplikasi dan menyediakan mekanisme untuk mengelola dan meminta catatan html. Di dalam berkas html terdapat file teks yang mendefinisikan struktur dan tata letak dengan placeheader guna mewakili konten aktual. 

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment merupakan alat yang digunakan untuk menjaga ruang terpisah pada sebuah proyek dengan pustaka dan dependensi di satu tempat. Proyek tersebut mempunyai kebutuhan yang berbeda antara satu dengan lainnya. Dengan demikian, virtual environment diperlukan karena dengan menggunakan virtual environment kita tidak perlu mengubah konfigurasi pada sistem informasi yang digunakan untuk menjalankan proyek tersebut.

    Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Kita dibebaskan dalam menggunakan virtual environment, termasuk menggunakan virtual environment di dalam repositori git lokal. Tetapi, kita harus menentukan file requirements.txt agar Heroku mengenal kebutuhan Python apa yang harus diinstal. Dalam  pembuatan requirements.txt akan lebih mudah jika menggunakan virtual environment.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas!
Yang saya lakukan untuk mengimplementasikan poin 1 sampai 4 adalah sebagai berikut:

    A. Permulaan
    1. Mengunjungi https://github.com/pbp-fasilkom-ui/assignment-repository untuk menggunakan template yang telah disediakan.
    2. Memasukkan nama repositori sesuai keinginan saya serta memastikan repositori saya bersifat public. Dalam hal ini saya menamai repositori saya "TUGAS_2_MEI".
    3. Clone repositori yang dibuat pada langkah 2 ke komputer dengan peritah "git clone https://github.com/hapsarimeilany/TUGAS_2_MEI.git"
    4. Masuk ke dalam repositori yang sudah saya clone di komputer saya dan membuat sebuah virtual environment dengan perintah "python -m venv env".
    5. Menyalakan virtual environment dengan perintah "env\Scripts\activate.bat" karena saya menggunakan perangkat Windows.
    6. Menginstall dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah "pip install -r requirements.txt".
    7. Mencoba menjalankan proyek Django yang telah dibuat dengan perintah "python manage.py runserver" dan membuka http://localhost:8000 untuk memastikan proyek Django yang saya buat telah berjalan dengan baik.

    B. Membuat Aplikasi Django beserta Konfigurasi Model
    1. Membuat django-app bernama katalog dengan perintah python manage.py startapp katalog. Namun, django-app tersebut telah dibuat dan tersedia di dalam template yang diberikan.
    2. Membuka settings.py di folder project_django dan menambahkan aplikasi katalog ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat ke dalam proyek Django.
    3. Membuka file models.py yang ada di folder katalog dan menambahkan potongan kode berikut:
        from django.db import models
        class CatalogItem(models.Model):
            item_name = models.CharField(max_length=255)
            item_price = models.BigIntegerField()
            item_stock = models.IntegerField()
            description = models.TextField()
            rating = models.IntegerField()
            item_url = models.URLField()
    4. Menjalankan perintah python manage.py makemigrations di cmd untuk mempersiapkan skema model ke dalam database Django lokal.
    5. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
    6. Membuat folder bernama fixture di dalam folder aplikasi katalog dan membuat sebuah berkas bernama initial_katalog_data.json yang berisi kode berikut:
        ```[
            {
                "model": "katalog.catalogitem",
                "pk": 1,
                "fields": {
                    "item_name": "iPhone 12 Pro Max",
                    "item_price": 17999999,
                    "description": "Original from iBox",
                    "item_stock": 3,
                    "rating": 5,
                    "item_url": "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb"
                }
            },
            {
                "model": "katalog.catalogitem",
                "pk": 2,
                "fields": {
                    "item_name": "MG Nu Gundam Ver.Ka",
                    "item_price": 1060000,
                    "description": "Bandai Original Ver.Ka Series",
                    "item_stock": 100,
                    "rating": 4,
                    "item_url": "https://www.tokopedia.com/hobbyjapan/mg-nu-gundam-verka"
                }
            },
            {
                "model": "katalog.catalogitem",
                "pk": 3,
                "fields": {
                    "item_name": "Samsung Galaxy S22",
                    "item_price": 12249000,
                    "description": "Specification: Snapdragon 8",
                    "item_stock": 1,
                    "rating": 5,
                    "item_url": "https://www.tokopedia.com/mhi-samsung/samsung-galaxy-s22-8-256gb-black"
                }
            },
            {
                "model": "katalog.catalogitem",
                "pk": 4,
                "fields": {
                    "item_name": "Nike Air Jordan Fasilkom",
                    "item_price": 3799000,
                    "description": "Nike Original Made In China",
                    "item_stock": 20,
                    "rating": 5,
                    "item_url": "https://www.tokopedia.com/807garage/air-jordan-1-mid-multicolour"
                }
            },
            {
                "model": "katalog.catalogitem",
                "pk": 5,
                "fields": {
                    "item_name": "Airpods Pro 3 Official Guarantee from iBox",
                    "item_price": 2999000,
                    "description": "Authorized Reseller",
                    "item_stock": 3,
                    "rating": 4,
                    "item_url": "https://www.tokopedia.com/tokobaruofficial/apple-airpods-3-mme73id-a-garansi-resmi-ibox"
                }
            }
        ]```

    7. Menjalankan perintah python manage.py loaddata initial_katalog_data.json untuk memasukkan data tersebut ke dalam database Django lokal.

C. Implementasi Views Dasar
1. Membuka views.py yang terletak di dalam folder katalog dan membuat sebuah fungsi yang menerima parameter request seperti berikut:      

       def show_katalog(request):
            return render(request, "katalog.html")

2. Membuat folder bernama templates di dalam folder aplikasi katalog dan membuat sebuah berkas dengan nama katalog.html. Isi dari katalog.html yaitu sebagai berikut:

        {% extends 'base.html' %}

        {% block content %}

        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        }

        td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
        }

        tr:nth-child(even) {
        background-color: #dddddd;
        }
        </style>
        </head>
        <body>

        <h1>Lab 1 Assignment PBP/PBD</h1>

        <h4>Name: {{nama}}</h4> 
        
        <h4>Student ID: {{NPM}}</h4>

        <table>
            <tr>
            <th>Item Name</th>
            <th>Item Price</th>
            <th>Item Stock</th>
            <th>Rating</th>
            <th>Description</th>
            <th>Item URL</th>
            </tr>
            {% comment %} Add the data below this line {% endcomment %}
        
        </table>

        {% endblock content %}

        </body>
        </html>
3. Membuat sebuah berkas di dalam folder aplikasi katalog dengan nama urls.py untuk menjalankan proses routing kepada fungsi views sehingga halaman HTML dapat terlihat di browser. 
        
       from django.urls import path
       from katalog.views import show_katalog

       app_name = 'katalog'

       urlpatterns = [
           path('', show_katalog, name='show_katalog'),
       ]

4. Mendaftarkan aplikasi katalog ke urls.py yang ada di folder project_django dengan menambahkan kode berikut ke variabel urlpatterns:

        ...
        path('katalog/', include('katalog.urls')),
        ...

5. Menjalankan proyek django dengan perintah "python manage.py runserver" dan melihat halaman yang telah dibuat pada browser dengan membuka `http://localhost:8000/wishlist/ `


D. Menghubungkan Models dengan Views dan Template
1. Mengimport models yang sudah dibuat sebelumnya pada fungsi views yaitu di dalam file views.py:

        from django.shortcuts import render
        from katalog.models import CatalogItem
        ...

2. Menambahkan potongan kode ke dalam fungsi show_katalog serta menambahkan "context" sebagai parameter ketiga pada return fungsi render:

        data_barang_katalog = CatalogItem.objects.all()
            context = {
            'list_barang': data_barang_katalog,
            'nama': 'Meilany',
            'NPM' : '2106751436'
        }
            return render(request, "katalog.html", context)

E. Mapping Data Untuk Memunculkan Fungsi views di HTML
1. Membuka file HTML pada folder templates di dalam direktori katalog.
2. Mengubah "Fill me!" dengan "{{nama}}" 
3. Melakukan iterasi terhadap variabel list_barang yang telah dirender ke dalam HTML:

        {% comment %} Add the data below this line {% endcomment %}
        {% for barang in list_barang %}
            <tr>
                <th>{{barang.item_name}}</th>
                <th>{{barang.item_price}}</th>
                <th>{{barang.item_stock}}</th>
            <th>{{barang.rating}}</th>
                <th>{{barang.description}}</th>
                <th><a href="{{barang.item_url}}">{{barang.item_url}}</a></th>
            </tr>
        {% endfor %}

4. Melakukan add, commit, dan push perubahan yang saya lakukan setelah memastikan halaman web berhasil menampilkan data yang dimasukkan ke dalam views.


F. Deployment Aplikasi ke Heroku
1. Membuat aplikasi bernama "katalogmeii" di Heroku
2. Menyalin API key akun saya pada aplikasi Heroku
3. Membuka Secrets pada repositori GitHub untuk GitHub Actions
4. Menambah repositori secret untuk melakukan deployment dengan memasukan nama aplikasi yang dibuat dan API key yang telah disalin:

        (NAM)HEROKU_APP_NAME
        (VALUE)APLIKASI-SAYA

5. Menjalankan kembali workflow yang gagal pada GitHub Actions.
6. Deployment sukses dan aplikasi berhasil dibuat. Dapat dikunjungi pada https://katalogmeii.herokuapp.com . Untuk melihat isi katalog dapat mengunjungi https://katalogmeii.herokuapp.com/katalog/ 



#### REFERENSI CODE:

https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro
