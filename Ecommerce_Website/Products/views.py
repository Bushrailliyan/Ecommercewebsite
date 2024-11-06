from django.shortcuts import render
from .forms import AddProductform
from .models import Product

# Create your views here.

def home(request):
    return render(request,'home.html')

def Add_Product(request):
    form = AddProductform()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    form = AddProductform()

    return render(request,'product_add.html',{'form':form})

def Update_Product(request):
    old_product = request.POST.get("oldname")
    old_price = request.POST.get("oldprice")
    new_product = request.POST.get("newname")
    new_price = request.POST.get("newprice")
    product_change = Product.objects.filter(name =old_product,price =old_price)
    if product_change.exists():
        product_change.update(name = new_product,price = new_price)
        return render(request,'update_product.html',{'msg':"Updated"})

    else:
        return render(request, 'update_product.html',{'msg':'No such Products'})



def Product_list(request):
    all_products = Product.objects.all()

    return render(request,'product_page.html',{'allproducts':all_products})

def Product_Detail(request):
    return render(request,'product_description.html')

def Company(request):
    return render(request,'company_homepage.html')



