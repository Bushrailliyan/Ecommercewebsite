from django.db import models
from USERS.models import Customer
from Products.models import Product
# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='cart')
    product =models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_items')


