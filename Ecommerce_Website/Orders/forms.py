from django import forms
from USERS.models import Customer

class CheckOutform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address','pincode','phone']

