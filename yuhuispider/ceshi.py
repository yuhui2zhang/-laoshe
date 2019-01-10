#!/user/bin/python3
# -*- coding : utf-8 -*-
import http.client as client
import json

from lxml import etree
import requests

data = """keyword: 
order: 0
city: 
recruitType: 
salary: 
experience: 
page: 1
positionFunction: 
_CSRFToken: 
ajax: 1"""

cookies = {
    'login_email': '2838031542%40qq.com', 'DJ_RF': 'empty', 'DJ_EU': 'http%3A%2F%2Fwww.dajie.com%2F',
    'DJ_UVID': 'MTU0NjUwMTU0NjQzNDk0NTUy', '_ga': 'GA1.2.1825000327.1546501501',
    '_gid': 'GA1.2.944145376.1546501501', '_close_autoreg': '1546501562208',
    '_close_autoreg_num': '2', '_ssytip': '1546501580883', 'dj_cap': '556208c566415fc725abf21d08a76739',
    'uchome_loginuser': '40320726', 'dj_auth_v3': 'MR6Z5iMAUiCa4bjJFlPxml35MHZyARWQg0q2PTV3puqwXL9qvyLfku4iWArS-5A*',
    'dj_auth_v4': 'dcd8d5f013e182c7266ba402aa8aadc2_pc', '_check_isqd': 'no',
    'Hm_lvt_6822a51ffa95d58bbe562e877f743b4f': '1546501501,1546501842',
    'USER_ACTION': 'request^AProfessional^AREG^A-^A-', 'Hm_lpvt_6822a51ffa95d58bbe562e877f743b4f': '1546503444',
    'SO_COOKIE_V2': 'c6b4a/PD1TBffnZfUSkeeGJ+qIZ8eRVFpWwQjfxEWDc+eW5jXlEGzaQctErOY6jU9oNhA18xo3SyOZ5JapGNPD0Mm5yuJGRk4qn9'
}

def get_params(data):
    params = {}
    for i in data.split('\n'):
        das = i.split(': ')
        params.update({das[0]: das[1]})
    return params

headers = """:authority: so.dajie.com
:method: GET
:path: /job/ajax/search/filter?keyword=&order=0&city=&recruitType=&salary=&experience=&page=1&positionFunction=&_CSRFToken=&ajax=1
:scheme: https
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
pragma: no-cache
referer: https://so.dajie.com/job/search?positionFunction=&positionName=Java
user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
x-requested-with: XMLHttpRequest"""


# if __name__ == '__main__':
#     with requests.session() as s:
#         url = 'https://so.dajie.com/job/ajax/search/filter'
#         params = get_params(data)
#         s.headers.update(get_params(headers))
#         s.proxies = {'http': '123.139.56.238:9999'}
#         # s.cookies.update(cookies)
#         text = s.get(url, params=params).content.decode('utf-8')
#         print(text)
#         # dict_data = json.loads(text)
#         # for li in dict_data['list']:
#         #     print(li)
#         # print(dict_data)

# if __name__ == '__main__':
#     with requests.session() as s:
#         s.headers = get_params(headers)
#         # s.cookies.update({
#         #     'DJ_EU': 'http://so.dajie.com/',
#         #     'DJ_RF': '',
#         #     'DJ_UVID': 'MTU0NjUwMTU0NjQzNDk0NTUy',
#         #     'Hm_lpvt_6822a51ffa95d58bbe562e877f743b4f': '1546562517',
#         #     'Hm_lvt_6822a51ffa95d58bbe562e877f743b4f': '1546501501,1546501842,1546562517',
#         #     'SO_COOKIE_V2': '86525HBUFnSkDKHSqwiKwjDHUp+u/4P8uGcnUk8yD+qFsGaZrM8WZ4dAMXa38j+eujhbi0U9bz4Rl0fZur3kQix+pV8VZ6xSvrm0',
#         #     '_check_isqd': 'no',
#         #     '_close_autoreg': '1546501562208',
#         #     '_close_autoreg_num': '2',
#         #     '_ga': 'GA1.2.1825000327.1546501501',
#         #     '_gat_gtag_UA_117102476_1': '1',
#         #     '_gid': 'GA1.2.944145376.1546501501',
#         #     '_ssytip': '1546562534061',
#         #     'login_email': '2838031542@qq.com'
#         # })
#         text = s.get('https://so.dajie.com/job/ajax/search/filter?keyword=&order=0&city=&recruitType=&salary=&experience=&page=2&positionFunction=&_CSRFToken=&ajax=1').text
#         print(text)




if __name__ == '__main__':
    conn = client.HTTPConnection(host='123.139.56.238', port='9999')
    conn.request('get', "https://so.dajie.com/job/ajax/search/filter?keyword=&order=0&city=&recruitType=&salary=&experience=&page=2&positionFunction=&_CSRFToken=&ajax=1", headers=get_params(headers))
    content = conn.getresponse()
    print(content)