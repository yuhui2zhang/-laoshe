import os

from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Page, Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pyecharts import Bar3D, Bar

import demo_sms_send

# Create your views here.
from user_app.models import User, TSj, MyLog
from tools import mylog, spider


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
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    code = request.POST.get('code','')
    if not code or code.lower() != request.session['captcha'].lower():
        return redirect('user:to_login')
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            request.session['user'] = user
            return redirect('user:to_main')
        raise ValueError
    except:
        return redirect('user:to_login')


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

@mylog
def to_menu(request):
    """
    进入menu页面
    :param request:
    :return:
    """
    ip = request.META.get('REMOTE_ADDR')
    user = request.session.get('user')
    username = user.username if user else ''
    if not spider(ip, username):
        return redirect('user:to_login')
    search = request.GET.get('search', 'search')
    city = request.GET.get('city', '')
    job = request.GET.get('job', '')
    page_index = request.GET.get('page_index', 1)
    li = TSj.objects.filter(city__contains=city, position__contains=job).order_by('id')
    # 判断用户是否已登录，若未登录，仅查询第一页数据
    page = Paginator(li, 10).page(page_index if request.session.get('user') else 1)
    return render(request, 'menu.html', {'page': page, 'search': search, 'val': (city or job) if search != 'search' else ''})


def to_main(request):
    """
    进入main页面
    :param request:
    :return:
    """
    return render(request, 'main.html', {})

def verify_code_for_phone(request):
    """
    发送手机验证码
    :param request: phone
    :return:
    """
    phone = request.GET.get('phone')
    verify_code = demo_sms_send.run(phone)
    # 设置验证码有效期为10分钟
    # request.set_cookie('verify_code',verify_code,max_age=60*10)
    return JsonResponse({})

def bar(request):
    """
    获取每个城市的每个职位的柱状图
    :param request:
    :return:
    """
    l = list()
    bar = Bar('计算机领域招聘信息柱状图','hello,i\'m 苍天有井',width=1200,height=600,background_color='pink',page_title='老舍就业分析网')
    citys = ['北京','上海','广州','深圳']
    kws = ['python web','爬虫','大数据','ai']
    for city in citys:
        l2 = list()
        for kw in kws:
            kw_list = TSj.objects.filter(city=city,position__icontains=kw )
            l2.append(len(kw_list))
        l.append(l2)
        l2 = list()
    (bar.add(citys[0], kws, l[0], is_stack=True, is_more_utils=True, yaxis_max=200)
     .add(citys[1], kws, l[1], is_stack=True, is_more_utils=True, yaxis_max=200)
     .add(citys[2], kws, l[2], is_stack=True, is_more_utils=True, yaxis_max=200)
     .add(citys[3], kws, l[3], is_stack=True, is_more_utils=True, yaxis_max=200))
    bar.render('templates/aa.html')
    return render(request,'aa.html')


def get_bar3d():
    """
    获取3d柱状图
    :return:
    """
    data = list()
    bar3d = Bar3D('计算机领域招聘信息柱状图', 'hello,i\'m 苍天有井', width=1200, height=600, background_color='pink',
                  page_title='老舍就业分析网', renderer='gif')
    citys = ['北京', '上海', '广州', '深圳']
    kws = ['python web', '爬虫', '大数据', 'ai']
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43',
                   '#d73027', '#a50026']
    for i in range(len(citys)):
        for j in range(len(kws)):
            data.append([i, j, len(TSj.objects.filter(city=citys[i], position__icontains=kws[j]))])
    print(data)
    bar3d.add(
        '招聘信息分布图',
        citys,
        kws,
        [[d[0], d[1], d[2]] for d in data],
        is_visualmap=True,
        is_grid3d_rotate=True,
        visual_range=[0, 20],
        visual_range_color=range_color,
        grid3d_width=200,
        grid3d_depth=80,
        is_more_utils=True,
    )
    return bar3d

REMOTE_HOST = "https://pyecharts.github.io/assets/js"
def bar3d(request):
    bar3d = get_bar3d()
    context = dict(
        myechart=bar3d.render_embed(),
        host=REMOTE_HOST,
        script_list=bar3d.get_js_dependencies()
    )
    return render(request,'bar3d.html',context=context)
