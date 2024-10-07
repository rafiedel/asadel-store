from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, JsonResponse
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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.core.paginator import Paginator

def check_authentication(request):
    if request.COOKIES == None:
        return redirect('login')
    
    response = HttpResponseRedirect(reverse('view_all_product'))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response

# ==========================================================================
# product nanti di get melalui fetchorigin api call di view all product html
# ==========================================================================
@login_required(login_url="login")
def view_all_product(request):
    # products = Product.objects.filter(user=request.user) 
    context = {
        # 'products': products,
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

@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    stock_available = strip_tags(request.POST.get("stock_available"))
    photo = strip_tags(request.POST.get("photo"))

    user = request.user
    new_product = Product(
        user=user, name=name, 
        price=price, description=description, 
        stock_available=stock_available, photo=photo
    )
    
    new_product.save()
    return HttpResponse(b"CREATED", status=201)

@login_required(login_url="login")
def edit_product(request, id):
    product = Product.objects.get(pk = id)

    if request.method == "POST":
        form  = ProductForm(request.POST , request.FILES, instance=product)

        if form.is_valid() :
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('view_all_product'))

    form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    mood = Product.objects.get(pk = id)
    mood.delete()
    return HttpResponseRedirect(reverse('view_all_product'))

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_products(request):
    # Get query parameters
    user_id = request.GET.get('id')
    page_number = request.GET.get('page')
    product_name = request.GET.get('product_name', '')

    # Ensure 'id' and 'page' are provided
    if not user_id or not page_number:
        return JsonResponse({'error': 'id and page are required'}, status=400)

    # Filter products by user and optionally by product_name if provided
    products_query = Product.objects.filter(user_id=user_id)
    if product_name:
        products_query = products_query.filter(name__icontains=product_name)

    # Paginate the fileterd Products
    paginator = Paginator(products_query, 8)
    try:
        page_obj = paginator.page(page_number)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    # Serialize data to a list of dictionaries instead of a JSON string
    data = list(page_obj.object_list.values('id', 'user_id', 'name', 'price', 'description', 'stock_available', 'photo'))
    
    # Provide min and max page from pagination
    min_page = 1
    max_page = paginator.num_pages

    # Return the serialized data along with pagination info
    context = {
        'products': data,  # Now it's a list of dictionaries, not a JSON string
        'min_page': min_page,
        'max_page': max_page,
    }
    return JsonResponse(context)


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
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('last_login')
    return response
