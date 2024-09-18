from django.db import models
from django.contrib.auth.models import User

class Product (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        default=1)
    name = models.CharField(
        max_length=30, 
        error_messages={'required': True})
    price = models.IntegerField(
        error_messages={'required': True})
    description = models.CharField(
        max_length=150,
        error_messages={'required': True})
    stock_available = models.IntegerField(
        error_messages={'required': True})
    photo = models.ImageField(
        blank=True, null=True, 
        upload_to='product_images/',
        error_messages={'required': False})
