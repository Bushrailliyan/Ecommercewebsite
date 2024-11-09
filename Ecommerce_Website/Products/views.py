from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import AddProductform
from .models import Product

# Create your views here.

def home(request):
    return render(request,'home.html')

def Showaccount(request):
    return render(request,'account.html')

def Add_Product(request):
    if request.method == 'post':
        form = AddProductform(request.post,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listproduct')
        else:
            print(form.errors)
    else:

        form = AddProductform()
        print(form.errors)

    return render(request,'product_add.html',{'form':form})

def Update_Product(request):
    old_product = request.POST.get("oldname")
    old_price = request.POST.get("oldprice")
    new_product = request.POST.get("newname")
    new_price = request.POST.get("newprice")
    product_change = Product.objects.filter(prod_name =old_product,price =old_price)
    #product_change = Product.objects.filter(name =old_product)
    if product_change.exists():
        product_change.update(prod_name = new_product,price = new_price)
        #product_change.update(name = new_product)
        return render(request,'update_product.html',{'msg':"Updated"})

    else:
        return render(request, 'update_product.html',{'msg':'No such Products'})

def RemoveProduct(request):
    prod_name = request.POST['name']
    prod_obj = Product.objects.filter(name =prod_name)
    prod_obj.delete()
    return render(request,'update_product.html',{'msg1':'Deleted'})


def Product_list(request):
    all_products = Product.objects.all()

    return render(request,'product_page.html',{'allproducts':all_products})

def Product_Detail(request):
    return render(request,'product_description.html')





