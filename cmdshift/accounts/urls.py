from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views





urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('info',views.info,name='info'),
    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile',views.profile,name='profile')

]
