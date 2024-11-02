from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
from Carts.models import CartItem
# Create your models here.
ORDER_STATUS =(
    ("ORDER CONFIRMED","order confirmed"),
    ("ORDER SHIPPED","order shipped"),
    ("ORDER DELIVERED","order delivered")
)

class OrderedItem(models.Model):
    user = models.ForeignKey(CartItem,on_delete=models.CASCADE,)
    product_details = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    order_status =models.CharField(max_length=20,choices=ORDER_STATUS,default=None)


