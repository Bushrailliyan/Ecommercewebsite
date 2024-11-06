from django.db import models
from django.contrib.auth.models import User

# Create your models here.
VERIFICATION =(
    ("APPROVED","approved"),
    ("REJECTED","rejected")

)


class Company(models.Model):
    user_name = models.OneToOneField(User,on_delete=models.CASCADE)
    co_name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=20,choices=VERIFICATION,default=None)

    def __str__(self):
         return self.co_name

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.IntegerField()
    phone = models.IntegerField()


    def __str__(self):
        return self.name