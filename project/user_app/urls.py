#!/user/bin/python3
# -*- coding : utf-8 -*-
from django.urls import path

from user_app import views

urlpatterns = [
    path('to/register/', views.to_register, name='to_register'),
    path('register/', views.register, name='register'),
    path('to/login/', views.to_login, name='to_login'),

]

