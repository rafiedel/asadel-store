from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def create_product(request):
    if request.method == "POST":
        form  = ProductForm(request.POST , request.FILES)

        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('view_all_product'))

    form = ProductForm()
    context = {'form': form}
    return render(request, "create_product.html", context)

def view_all_product(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'npm': '2306245485',
        'name': 'Rafie Asadel Tarigan',
        'class': 'F'
    }
    return render(request, "view_all_product.html", context)

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