from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect

def check_authentication(request):
    if request.COOKIES == None:
        return redirect('login')
    
    response = HttpResponseRedirect(reverse('view_all_product'))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response

@login_required(login_url="login")
def view_all_product(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'products': products,
        'npm': '2306245485',
        'name': request.user.username,
        'class': 'F',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "view_all_product.html", context)

@login_required(login_url="login")
def create_product(request):
    if request.method == "POST":
        form  = ProductForm(request.POST , request.FILES)

        if form.is_valid() :
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('view_all_product'))

    form = ProductForm()
    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    mood = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('view_all_product'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    mood = Product.objects.get(pk = id)
    mood.delete()
    return HttpResponseRedirect(reverse('view_all_product'))

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
