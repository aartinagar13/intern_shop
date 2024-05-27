from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
   # path('home/', views.homeindex, name='home'),
   # path('login/', views.login_view, name='login'),
    path('resetpwd/', views.resetpwd, name='resetpwd'),
    path('registration/', views.register, name='register'),
]
   
