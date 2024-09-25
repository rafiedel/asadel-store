# ASADEL STORE - Tugas Individu PBP

## Daftar Isi
- [Identitas Mahasiswa](#identitas-mahasiswa)
- [Link Website](#link-website)
- [Tugas Individu 2 : Implementasi Model-View-Template (MVT) pada Django](#tugas-individu-2-implementasi-model-view-template-mvt-pada-django)
- [Tugas Individu 3 : Implementasi Form dan Data Delivery pada Django](#tugas-individu-3--implementasi-form-dan-data-delivery-pada-django)
- [Tugas Individu 4 : Implementasi Autentikasi, Season, dan Cookies pada Django](#tugas-individu-4--implementasi-autentikasi-session-dan-cookies-pada-django)

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

### A. Perbedaan HttpResponseRedirect() dan redirect()

Hasil dari HttpResponseRedirect() dan redirect() sama, yaitu mengarahkan user ke ke url yang dituju. Akan tetapi, redirect() lebih simpel, karena HttpResponseRedirect() perlu menggunakan reverse() untuk menyatakan url tujuan, sedangkan redirect() tidak.

### B. Menghubungkan Model dengan User

Menghubungkan model dengan user dilakukan dengan cara membuat field yang berisi model.ForeignKey(). Di dalamnya tersebut kita assign class User agar model mengetahui bahwa ForeignKey tersebut diperuntukan untuk User. Secara default, ketika model tersebut dibuat, model akan mencantumkan id User.

### C. Autentikasi dan Otorisasi

Autentikasi digunakan saat user login dengan tujuan agar masukan username dan password valid sehingga user dapat menggunakan akun yang sesuai saat mengakses platform. Otorisasi adalah cara kerja platform untuk menentukan apakah suatu halaman dapat diakses oleh akun yang digunakan user.

### D. Penggunaan dan Tingkat Keamanan Cookies

Cookies digunakan untuk mengingat akun user di browser, agar kemudian user dapat mengakses kembali tanpa login ulang. Selain menyimpan akun user, cookies dapat digunakan juga untuk menyimpan prefrensi user (contohnya teman dan bahasa) dan melacak aktivitas pengguna sebagai data untuk dianalisis pemilik dari platform tersebut (contohnya halaman apa saja yang sering dikunjugni user)


### E. Cara Implementasi Checklist

1. Menghubungkan model Product dengan User di *main/models.py* lalu migrasi
```python
class Product (models.Model):
   user = models.ForeignKey(
      User, on_delete=models.CASCADE, 
      default=1)
   ...
```

2. Di Views menambahkan dan mengubah beberapa views.
- Menambahkan views untuk login, logout, dan registrasi.
```python
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)
def login_user(request):
    next_url = (request.GET.get('next', '/'))[1:].replace('-', '_')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse(next_url))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            print(next_url + "-")
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('last_login')
    return response
```
- Menambahkan kondisi bahwa user perlu login untuk mengakses views ke suatu halaman
```python
@login_required(login_url="login")
def view_all_product(request):
   ...

@login_required(login_url="login")
def create_product(request):
   ...
```

- Mengubah views create_product agar produk yang dibuat dapat tidak langsung di-save dan bisa menghubungkan produk ke user
```python
if form.is_valid() :
   product = form.save(commit=False)
   product.user = request.user
   product.save()
   ...
```

- Mengubah views view_all_product agar product yang diambil hanya produk yang terhubung dengan user tersebut, mengirim data cookies last login dan username user.
```python
...
products = Product.objects.filter(user=request.user)

context = {
   'products': products,
   'npm': '2306245485',
   'name': request.user.username,
   'class': 'F',
   'last_login': request.COOKIES['last_login'],
}
...
```

- Menambahkan views check_authentication agar ketika user masuk ke akar url, akan langsung diarahkan ke view_all_product (bila id user terdapat di cookies) atau ke login (bila id user tidak terdapat di cookies)
```python
def check_authentication(request):
   if request.COOKIES == None:
      return redirect('login')
   
   return redirect('view_all_product')
```

3. Menambahkan konfigurasi urls views yang sudah dibuat
```python
urlpatterns = [
    path('', check_authentication, name=''),
    .... 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

4. Menambahkan halaman registrasi dan login serta Mengubah halaman views_all_product

- *login.html*
```html
{% extends 'app.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'register' %}">Register Now</a>
</div>

{% endblock content %}
```
- *register.html*
```html
{% extends 'app.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
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
- *view_all_product.html*
```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
<a href="{% url 'logout' %}">
    <button>Logout</button>
</a>
...
```
3. Membuat 3 Dummy Data untuk masing-masing User (Dua User)

![ERROR](README_IMAGES/tugas3/dummy1.png)
![ERROR](README_IMAGES/tugas3/dummy2.png)
