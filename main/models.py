from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=150)
    stock_available = models.IntegerField(default=0)
    
'''
    IDE KACAU :v

class User(models.Model):
    name = models.CharField(max_length=30)

class Juragan(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    products = models.ManyToManyField('Product', related_name='juragan_products')

class Product(models.Model):
    owner = models.ForeignKey(Juragan, on_delete=models.CASCADE, related_name='owned_products')
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=150)
    stock_available = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, related_name='cart_products')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1)  
    comment = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

class History(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_history')
    seller = models.ForeignKey(Juragan, on_delete=models.CASCADE, related_name='sales_history')
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    buyer_address = models.CharField(max_length=255)
    seller_address = models.CharField(max_length=255)

'''