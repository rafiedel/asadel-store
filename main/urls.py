from django.urls import include, path
from .views import show_main

urlpatterns = [
    path('', show_main, name='show_main'),
]