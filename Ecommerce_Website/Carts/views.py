from django.shortcuts import render

# Create your views here.

def Cart_display(request):
    return render(request,'cart_page.html')
