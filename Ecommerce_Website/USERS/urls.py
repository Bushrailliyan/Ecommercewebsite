from django.urls import path
from .import views

urlpatterns = [
    path('',views.CompanySignup,name='co-signup'),
    path('cust_signup',views.CustomerSignup,name='custsignup'),
    path('co_home',views.Company,name='company_home'),

]