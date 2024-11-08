from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Company

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
        company = authenticate(username=u_name, password=passwd)
        if company is not None:
            login(request, company)
            return redirect('company_home')
        else:
            return redirect('home')

    return render(request,'company_signup.html')

def Company(request):
    return render(request,'company_homepage.html')