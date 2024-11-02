from django.db import models

from USERS.models import Company


# Create your models here.

class Product(models.Model):
    prod_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='media')
    stock_qty = models.IntegerField(default=1)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_name






