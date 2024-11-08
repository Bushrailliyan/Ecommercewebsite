from django.urls import path
from .import views

urlpatterns = [
    path('',views.CompanySignup,name='co-signup'),
    path('co_home',views.Company,name='company_home'),

]