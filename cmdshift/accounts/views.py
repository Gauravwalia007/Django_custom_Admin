from django.shortcuts import render,redirect
from .models import Users
from django.contrib import messages


def home(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':
        user=Users()
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.mobno=request.POST['mobno']
        user.image=request.POST['image']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user.password=password1
            if Users.objects.filter(username=user.username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif Users.objects.filter(email=user.email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user.save()
                print("user created")
                return redirect('info')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def info(request):
    if request.method=='POST':
        return redirect('/')
    else:
        user=Users.objects.all().last()
        return render(request,'info.html',{'user':user})   
