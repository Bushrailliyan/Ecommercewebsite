from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    user_name = models.OneToOneField(User,on_delete=models.CASCADE)
    co_name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=15,blank=True,null=True,default=None)
    email = models.EmailField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
         return self.co_name

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=15,default=None)
    phone = models.CharField(max_length=15,blank=True,null=True,default=None)


    def __str__(self):
        return self.name