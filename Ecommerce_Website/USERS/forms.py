from django import forms
from USERS.models import Customer
from USERS.models import Company


class CompanySignupForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['user_name','co_name','address','phone','email','password']
