from django.db import models

class Product (models.Model):
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
