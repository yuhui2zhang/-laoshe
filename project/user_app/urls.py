#!/user/bin/python3
# -*- coding : utf-8 -*-
from django.urls import path

from user_app import views

urlpatterns = [
    path('to/register/', views.to_register, name='to_register'),
    path('register/', views.register, name='register'),
    path('to/login/', views.to_login, name='to_login'),
    path('login/', views.login, name='login'),
    path('get_captcha/', views.get_captcha, name='get_captcha'),
    path('to/menu/', views.to_menu, name='to_menu'),
    path('to/main/', views.to_main, name='to_main'),
    path('verify_code_for_phone/', views.verify_code_for_phone, name='verify_code_for_phone'),
    path('bar/', views.bar, name='bar'),
    path('bar3d/', views.bar3d, name='bar3d'),
]

