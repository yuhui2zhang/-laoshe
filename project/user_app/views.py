from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def to_register(request):
    """
    进入注册页面
    :param request:
    :return: s
    """
    return render(request, 'register.html', {})


def register(request):
    """
    注册的逻辑处理
    :param request:
    :return:
    """
    username = request.POST.get('userid')
    phone = request.POST.get('usrtel')
    email = request.POST.get('email')
    psw = request.POST.get('psw')
    print(username, phone, email, psw)
    return HttpResponse(123)


def to_login(request):
    """
    进入登录页面
    :param request:
    :return:
    """
    return render(request, 'login.html', {})
