from django.shortcuts import redirect
from django.urls import path
from .views import check_authentication, create_product, create_product_ajax, edit_product, delete_product, view_all_product,show_xml, show_json, show_xml_by_id, show_json_by_id, get_products, register, login_user, logout_user

urlpatterns = [
    path('', check_authentication, name=''),
    path('view-all-product', view_all_product, name='view_all_product'),
    path('create-product', create_product, name='create_product'),
    path('create-product-ajax', create_product_ajax, name='create_product_ajax'),
    path('edit-product/<str:id>', edit_product, name='edit_product'),
    path('delete/<str:id>', delete_product, name='delete_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-products/', get_products, name='get_products'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
