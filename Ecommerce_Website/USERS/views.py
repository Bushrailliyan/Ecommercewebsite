from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Company,Customer

# Create your views here.
def CompanySignup(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST['username']
            company_name = request.POST['companyname']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            password = request.POST['password']
            company_user = User.objects.create_user(username=username, password=password)
            company = Company(user_name=company_user, co_name=company_name, email=email, address=address, phone=phone)
            company_user.save()
            company.save()
            return HttpResponse("You have been registered successfully")

        except Exception as e:
            print(e)
            return HttpResponse("Invalid user details")



    if request.POST and 'login' in request.POST:
        u_name = request.POST['username']
        passwd = request.POST['password']
        co_user = authenticate(username=u_name, password=passwd)
        if co_user is not None:
            login(request, co_user)
            return redirect('company_home')
        else:
            return redirect('home')

    return render(request,'company_signup.html')

def Company(request):
    return render(request,'company_homepage.html')






# Customer part

def CustomerSignup(request):
    if request.POST and 'register' in request.POST:
        try:
            uname = request.POST['username']
            customer_name = request.POST['customername']
            adres = request.POST['address']
            pin_code = request.POST['pincode']
            phone_no = request.POST['phone']
            pass_word = request.POST['password']
            customer_user = User.objects.create_user(username=uname,password=pass_word)
            customer = Customer(user = customer_user,name = customer_name,address = adres,pincode = pin_code,phone = phone_no)
            customer_user.save()
            customer.save()
            return HttpResponse("You have been registered successfully")

        except Exception as e:
            print(e)
            return HttpResponse("Invalid user details")

    if request.POST and 'login' in request.POST:
        u_name = request.POST['username']
        paswrd = request.POST['password']
        buyer_user = authenticate(username = u_name,password =paswrd)
        if buyer_user is not None:
            login(request, buyer_user)
            return redirect('addcart')
        else:
            return redirect('home')

    return render(request,'customer_signup.html')







