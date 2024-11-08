from django.db import models
from django.contrib.auth.models import User
from USERS.models import Customer
from Products.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    order = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart')
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name




