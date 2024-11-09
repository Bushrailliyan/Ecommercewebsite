from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
from Carts.models import CartItem
# Create your models here.
ORDER_STATUS =(
    ("Order Pending","order pending"),
    ("Order Shipped","order shipped"),
)

class OrderedItem(models.Model):
    user = models.ForeignKey(CartItem,on_delete=models.CASCADE,related_name='orders')
    product_details = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    order_status =models.CharField(max_length=20,choices=ORDER_STATUS,default='Order Pending')


