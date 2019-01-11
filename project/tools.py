#!/user/bin/python3
# -*- coding : utf-8 -*-
import time
from django.utils.timezone import now, timedelta
from user_app.models import MyLog
from datetime import datetime, date


def mylog(func):
    """
    保存日志
    :param func:
    :return:
    """
    def in_fun(request):
        ip = request.META.get('REMOTE_ADDR')
        url = request.META.get('PATH_INFO')
        method = request.META.get('REQUEST_METHOD')
        user = request.session.get('user')
        username = user.username if user else ''
        MyLog.objects.create(user_ip=ip, request_url=url, username=username, create_time=now().date(), method=method)
        return func(request)
    return in_fun


def spider(user_ip, username):
    """
    反爬虫
    :param user_ip:
    :param username:
    :return:
    """
    log_list = MyLog.objects.filter(user_ip=user_ip, create_time__gt=time.time()-10*60).count()
    count = MyLog.objects.filter(username=username, create_time__gt=time.time() - 10 * 60).count()
    if log_list <= 10 or count <= 10:
        return True
