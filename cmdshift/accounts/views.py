from django.shortcuts import render,redirect,HttpResponse
from .models import Users
from django.contrib import messages
from .forms import RegistrationForm


def home(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})
    else:
        form = RegistrationForm()
        return render(request,'register.html',{'form':form})



def info(request):
    if request.method=='POST':
        return redirect('/')
    else:
        user=Users.objects.all().last()
        return render(request,'info.html',{'user':user})

def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})

