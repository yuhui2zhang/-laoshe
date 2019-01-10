import os

from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Page, Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user_app.models import User, TSj

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
    :param request:用户名：username     手机：phone    邮箱：email    密码：psw      加密方式：django自带的加密方式
    :return:用户名存在返回注册页面，用户名不存在注册成功返回登录页面
    """
    username = request.POST.get('userid')
    phone = request.POST.get('usrtel')
    email = request.POST.get('email')
    psw = request.POST.get('psw')
    password = make_password(psw)
    try:
        User.objects.get(username=username)
    except:
        User.objects.create(username=username, password=password, email=email, phone=phone)
        return redirect('user:to_login')
    return redirect('user:to_register')


def to_login(request):
    """
    进入登录页面
    :param request:
    :return:
    """
    return render(request, 'login.html', {})


def login(request):
    """
    登录的逻辑处理
    :param request:
    :return:
    """
    print(123)
    username = request.POST.get('username')
    password = request.POST.get('password')
    code = request.POST.get('code')
    if code.lower() != request.session['captcha'].lower():
        return redirect('user:to_login')
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            return HttpResponse('=================华丽分割西线=====================')
            # return redirect('user:main')
        raise ValueError
    except:
        return redirect('user:to_main')


def get_captcha(request):
    """
    更换并生成验证码图片
    :param request:
    :return:
    """
    from static.captcha.image import ImageCaptcha
    image = ImageCaptcha(fonts=[os.path.abspath("captcha/fonts/JOKERMAN.TTF")])
    import random, string
    # random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 5)
    # 随机码
    code = "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 4))
    data = image.generate(code)
    request.session['captcha'] = code
    # request.META.update({'captcha':code})
    # print(request.META['captcha'])
    return HttpResponse(data, "image/png")

def to_menu(request):
    """
    进入menu页面
    :param request:
    :return:
    """
    search = request.GET.get('search', 'search')
    city = request.GET.get('city', '')
    job = request.GET.get('job', '')
    page_index = request.GET.get('page_index', 1)
    li = TSj.objects.filter(city__contains=city, position__contains=job)
    page = Paginator(li, 10).page(page_index)
    return render(request, 'menu.html', {'page': page, 'search': search, 'val': (city or job) if search != 'search' else ''})

def to_main(request):
    """
    进入main页面
    :param request:
    :return:
    """
    return render(request, 'main.html', {})

