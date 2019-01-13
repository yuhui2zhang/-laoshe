# -*- coding: utf-8 -*-
import random
import string

from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT

"""
短信业务调用接口示例，版本号：v20170525
Created on 2017-06-12

"""
ACCESS_KEY_ID = "LTAIG5hUDXMqkDpI"
ACCESS_KEY_SECRET = "PpKskwqK7Lb4YOqJKPrRDzf1W5apd5"
# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


def send_sms(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(sign_name)

    # 数据提交方式
    # smsRequest.set_method(MT.POST)

    # 数据提交格式
    # smsRequest.set_accept_format(FT.JSON)

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)

    # TODO 业务处理

    return smsResponse

def run(phone):
    __business_id = uuid.uuid1()
    # print(__business_id)
    # params = "{\"code\":\"123456\"}"\
    # params = u'{"code":"AI137的全体学生在班长的带领下祝你新年快乐！"}'
    code = ''.join(random.sample(string.digits,4))
    params = u'{"code":"' + code + '"}'
    # print(send_sms(__business_id, "18910252862", "广告", "SMS_29435071", params).decode('utf-8'))
    # print(send_sms(__business_id, phone, "广告", "SMS_29435071", params).decode('utf-8'))
    send_sms(__business_id, phone, "广告", "SMS_29435071", params).decode('utf-8')
    return code

if __name__ == '__main__':
    run('18875011303')




