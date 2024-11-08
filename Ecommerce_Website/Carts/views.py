from django.shortcuts import render

# Create your views here.

def Add_to_Cart(request):

    return render(request,'cart_page.html')

def Cart_display(request):
    return render(request,'cart_page.html')
