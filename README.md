# ASADEL STORE - Tugas Individu PBP

## Daftar Isi
- [Identitas Mahasiswa](#identitas-mahasiswa)
- [Link Website](#link-website)
- [Tugas Individu 2 : Implementasi Model-View-Template (MVT) pada Django](#tugas-individu-2-implementasi-model-view-template-mvt-pada-django)
- [Tugas Individu 3 : Implementasi Form dan Data Delivery pada Django](#tugas-individu-3--implementasi-form-dan-data-delivery-pada-django)

## Identitas Mahasiswa

**Nama**: Rafie Asadel Tarigan  
**NPM**: 2306245485  
**Kelas**: PBP - F

## Link Website

Website dapat diakses melalui:  
http://rafie-asadel-asadelstore.pbp.cs.ui.ac.id/

## Tugas Individu 2 : Implementasi Model-View-Template (MVT) pada Django

### A. Cara Implementasi Checklist Tahapan Pengerjaan Tugas
Berikut adalah langkah-langkah implementasi checklist secara detail:

1. **Setup Kebutuhan**
   - Buat env dengan 
```bash
    python -m venv env
    env\Scripts\activate
```
   - Buat dan isi file requirements.txt dengan libraries yang ingin di install, lalu jalankan
```bash
    pip install -r requirements.txt
```

2. **Setup Proyek Django**
   - Buat proyek dengan 
```bash
  django-admin startproject asadelstore
```
   - Masuk ke direktori proyek dengan .
```bash
  cd asadelstore
```

3. **Buat Aplikasi**
   - Buat aplikasi dengan 
```bash
python manage.py startapp main
```
   - Di dalam *`asadelstore/settings.py`* lakukan perubahan dengan isi
```python
INSTALLED_APPS = [
     ...,
    'main', 
    ]
```

4. **Definisikan Model**
   - Di dalam *`main/models.py`*, buat model Product beserta fieldnya,
   - Jalankan migrasi menggunakan 
```bash
python manage.py makemigrationspython manage.py migrate
```

5. **Buat Views**
   - Di dalam *`main/views.py`* buat fungsi `show_main` untuk mengirim data sekaligus menampilkan halaman main.html
```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'npm' : '2306245485',
            'name': 'Rafie Asadel Tarigan',
            'pbp_class': 'F'
        }

        return render(request, "main.html", context)
```

6. **Tentukan URL Patterns**
   - Di dalam *`asadel/urls.py`* tambahkan kode berikut agar proyek langsung melanjutkan routing ke urlpatterns di aplikasi
```python
    urlpatterns = [
        ...
        path('', include('main.urls'))
    ]
```
   - Buat file *`main/urls.py`* dan tambahkan kode berikut agar routing langsung mengeksekusi fungsi `show_main`
```python
    from django.urls import include, path
    from .views import show_main

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
```

7. **Desain Template HTML**
   - Buat folder serta file *`main/templates/main.html`* tampilkan data dengan
```html
    ...
    </body>
    <footer>
        @ {{ name }} | NPM {{ npm }} | F - {{ pbp_class }}
    </footer>
</html>
```

### B. Alur Kerja Request dan Respon pada Django

![ERROR](README_IMAGES/tugas2/django.png)

#### Client -> URL Configuration -> Views -> Model -> BasisData
1. **Client** mengirim permintaan (request) yang akan diterima oleh URL proyek.
2. **URL Configuration** akan meneruskan permintaan ke URL aplikasi.
3. **URL** akan memeriksa daftar permintaan (URL patterns) untuk mencocokkan permintaan dari Client.
4. Jika ditemukan, URL akan mengeksekusi **View** yang terdaftar untuk permintaan tersebut.
5. **View** akan menggunakan **Model** untuk berinteraksi dengan data di **Basis Data**.
6. **Model** akan melakukan pemetaan data di **Basis Data** sesuai perintah dari View.

#### BasisData -> Model -> Views -> Template -> Client
1. Setelah perintah selesai diproses, **Model** akan mengirimkan data kembali dari **Basis Data**.
2. **View** akan menerima data dan memilih **Template** untuk menyajikan data tersebut.
3. **Template** akan menggabungkan data dan format HTML untuk menghasilkan halaman web.
4. Halaman web yang sudah jadi akan dikirimkan kembali sebagai **respon** ke **Client**.
5. **Client** menerima respon dan menampilkan hasilnya.




### C. Fungsi Git dalam Pengembangan Perangkat Lunak

1. **Version Control**
   - **Melacak Perubahan**: Git mencatat perubahan kode, memungkinkan untuk kembali ke pengerjaan sebelumnya.

2. **Collaboration**
   - **Berkolaborasi**: Memudahkan banyak pengembang bekerja pada proyek yang sama dengan mengelola perubahan dan mengatasi konflik.

3. **Branching and Merging**
   - **Branching**: Membuat cabang terpisah agar untuk pengerjaan setiap fitur dan menjaga kode utama tetap stabil.
   - **Merging**: Menggabungkan cabang kembali ke kode utama setelah suatu fitur selesai.

4. **History Tracking**
   - **Riwayat Perubahan**: Membantu dalam audit dan debugging dari semua catatan perubahan dan informasi

5. **Distributed Development**
   - **Sistem Terdistribusi**: Setiap menyalin dan memulihkan data repository ke ruang kerja lokal.

6. **Integrasi dengan Alat Lain**
   - **CI/CD dan Code Review**: Alat otomatisasi dan review kode untuk meningkatkan dan memudahkan proses pengembangan.


### D. Django Menjadi Framework Awal untuk Belajar Pengembangan Perangkat Lunak

1. **Gentle Learning Curve**
   - **Mudah Dipelajari**: Struktur proyek yang sederhana memudahkan pemula mengenal cara pembuatan perangkat lunak
2. **Python Based**
   - **Bahasa Python**: Python yang merupakan salah satu bahasa pemrograman tingkat tinggi yang mudah dikuasai
3. **Good Documention and Community**
   - **Dokumentasi**: Dokumentasi django sangat lengkap dan terstruktur
   - **Komunitas**: Sudah banyak pengembang yang menggunakan sehingga mudah mencari informasi di berbagagi platform tech
4. **Built-in Feature**
   - **Fitur Siap Pakai**: Django sudah disediakan berbagai fitur siap pakai untuk memudahkan dan mempercepat proses pengembangan

### E. Model Django Disebut ORM

ORM *(Object-Relational Mapping)* adalah teknik pengembangan perangkat lunak yang menghubungkan suatu kelas objek ke kolom, baris, dan tabel di suatu basis data menjadi sebuah data. 

Dalam Django, pengembang menggunakan bahasa pemrograman Python untuk CRUD (membuat, mengambil, memperbarui, dan menghapus) data tanpa menulis SQL secara langsung. Jadi, Django secara otomatis mengelola pemetaan data-data di basis data tersebut, sedangkan pengembang bisa fokus membuat kode pemrograman Python.

## Tugas Individu 3 : Implementasi Form dan Data Delivery pada Django

### A. *Data Delivery* untuk Platfrom

Tujuan utama user mengakses sebuah platform adalah untuk melihat informasi, sedangkan informasi tersebut hanya diambil melalui server. Dengan *data delivery* platform dapat mengirim permintaan ke server lalu dikembalikan dalam bentuk respon sesuai permintaannya. Pada akhirnya, platform akan menampilkan respon yang dikirim oleh server.

### B. JSON dan XML

Dalam konteks *data delivery* akan lebih memudahkan developer mengolah data format JSON untuk dapat ditampilkan kepada user. Hal tersebut karena strukturnya yang lebih simple dan mudah dibaca, ukuran data lebih kecil, dan lebih cepat diparsing daripada XML. Maka dari itu, format JSON lebih sering dipakai untuk mengirim data melalui API.

### C. Method is_valid()

Method tersebut adalah bawaan django yang berfungsi untuk memvalidasi semua input agar tidak terkena error ketika disimpan. Dengan method tersebut, kita telah dimudahkan agar tidak perlu membuat logic validasi input lagi.

### D. Komponen csrf_token untuk Formulir Django

Komponen tersebut sangat diperlukan untuk menjaga keamanan data. Bila tidak ada itu, maka dapat dilakukan penyerangan CSRF (*Cross-Site Request Forgery*). Hal tersebut dapat dimanfaatkan oleh penyerang untuk mengirim permintaan yang berbahaya, seperti mengirim malware ke basis data.

### E. Cara Implementasi Jawaban dari Tugas3 A-D
1. **Setup Form**
   - Membuat file *forms.py* di dalam *main* dan isi dengan
   ```python
   from django import forms
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock_available", "photo"]
   ```
   - Membuat views nya dengan mengupdate *views.py* dengan
   ```python

   def create_product(request):
      if request.method == "POST":
         form  = ProductForm(request.POST , request.FILES)

         if form.is_valid() :
               form.save()
               return HttpResponseRedirect(reverse('view_all_product'))

      form = ProductForm()
      context = {'form': form}
      return render(request, "create_product.html", context)
   ```
   - Tambahkan routing dari views diatas dengan
   ```python
   urlpatterns = [
      ...
      path('create-product', create_product, name='create_product'),
      ...
   ]
   ```
   - Membuat file *app.html* di folder *templates* dan isi dengan
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
      <head>
         <meta charset="UTF-8" />
         <meta
               name="viewport"
               content="width=device-width, initial-scale=1.0"
         />
         <link rel="stylesheet" href="{% static 'styles/style.css' %}">
         {% block meta %}
         {% endblock meta %}
      </head>

      <body>
         {% block content %}
         {% endblock content %}
      </body>
   </html>
   ```
   - Lalum, membuat file *create_all_product.html* di folder *templates* dan isi dengan
   ```html
   {% extends 'app.html' %} 

   {% block content %}
   <h1>Add New Product</h1>

   <form method="post" enctype="multipart/form-data">
      {% csrf_token %}
      <table>
         {{ form.as_table }}
         <tr>
               <td></td>
               <td>
                  <input type="submit" value="Add Product"/>
               </td>
         </tr>
      </table>
   </form>

   {% endblock %}
   ```
2. **Views Pengambilan Data dalam Format XML dan JSON**
   - Untuk menampilkan data dalam format XML dan JSON (All mauapun by id) dapat dilakukan dengan mengupdate *views.py* dengan
   ```python
   ...
   def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_xml_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

3. **Membuat Routing Views dari Point 2**
   - Setelah itu, inisialisasi routing agar dapat menjalankan views tersebut
   ```python
   urlpatterns = [
      ...
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'), 
      path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), 
   ]
   ```

### F. Bukti Respon Views di Postman
![ERROR](README_IMAGES/tugas3/json.png)
![ERROR](README_IMAGES/tugas3/json_id.png)
![ERROR](README_IMAGES/tugas3/xml.png)
![ERROR](README_IMAGES/tugas3/xml_id.png)


## Tugas Individu 4 : Implementasi Autentikasi, Session, dan Cookies pada Django

## A. Django UserCreationForm
- adalah...
- apa kelebihan dan kekurangannya
## B. Autentikasi dan Otorisasi dalam Django
- perbedaan keduanya
- mengapa keduanya penting
### C. Cookies pada Web
- apa itu cookies
- bagaimana django mengulah cookies untuk mengelola data sesi pengguna
### D. Keamanan Cookies
- apakah aman secara default
- apakah ada resiko potensial yang harus diwaspadai

### E. Cara Implementasi Jawaban dari Tugas4 A-D