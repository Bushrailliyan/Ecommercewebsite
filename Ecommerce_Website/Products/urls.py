from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('prod_list',views.Product_list,name='listproduct'),
    path('prod_detail',views.Product_Detail,name='product_details'),
    #path('company',views.Company,name='company_home'),
    path('add_product',views.Add_Product,name='addproduct'),
    path('update_product',views.Update_Product,name='updateproduct'),


]