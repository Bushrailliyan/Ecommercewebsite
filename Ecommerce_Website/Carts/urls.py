from django.urls import path
from .import views

urlpatterns = [
    path('',views.Add_to_Cart,name='addcart'),
    path('',views.Cart_display,name='carts'),

]