import requests
from bs4 import BeautifulSoup
import lxml

from selenium import webdriver
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import re
import time

def time_switch(give_day):
    day = 20210300 + int(give_day) * 7 - 7
    if int(give_day) == 1:
        day = 20210301
    str_day = f"{day}"
    while int(str_day[6:8]) >= 31:
        day = day + 100

        if int(str_day[4:6]) < 8:
            if int(str_day[4:6]) % 2 != 0:  # 奇数
                next_month = int(str_day[6:8]) - 31

                day = int(day - int(str_day[6:8]))
                day = day + next_month
                # print(day)
                str_day = f"{day}"

            else:
                next_month = int(str_day[6:8]) - 30

                day = int(day - int(str_day[6:8]))
                day = day + next_month
                # print(day)
                str_day = f"{day}"

        else:
            if int(str_day[4:6]) % 2 != 0:  # 奇数
                next_month = int(str_day[6:8]) - 30

                day = int(day - int(str_day[6:8]))
                day = day + next_month
                # print(day)
                str_day = f"{day}"
            else:
                next_month = int(str_day[6:8]) - 31

                day = int(day - int(str_day[6:8]))
                day = day + next_month
                # print(day)
                str_day = f"{day}"

    dayed = f"{str_day[0:4]}" + "-" + f"{str_day[4:6]}" + "-" + f"{str_day[6:8]}"
    return dayed

def get_schedule(give_day):


    dayed = time_switch(give_day)
    # day = {
    #     "3":"2021-03-14",
    # }
    # _cookies = login()
    # headers = {
    #     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    #     # 'cookie':_cookies,
    #     'cookie':"JSESSIONID=BE2E5A9346699C5A60AAB8292AAE12BD; UM_distinctid=17718c323ff1fa-01b23d4de28f12-31346d-144000-17718c32400b8a; SERVERID=122; JSESSIONID=C4A7A40F669203335DCF52C7BBE75858",
    #     'Connection':"keep-alive",
    #
    # }
    #
    # url = f"http://jwgl.qziedu.cn/jsxsd/framework/main_index_loadkb.jsp?rq={dayed}&sjmsValue=A3B9D58CF4AD4C97B59C1E0DEA2AB2B6"
    #
    # total = []
    #
    # response = requests.get(url=url,headers=headers)
    # text = response.text
    # print(response.status_code)

    LOGIN_URL = 'http://jwgl.qziedu.cn/jsxsd/xk/LoginToXk'
    values = {'userAccount': '2003010533', 'userPassword': 'Zhy13719218332',
              'encoded': 'MjAwMzAxMDUzMw==%%%Wmh5MTM3MTkyMTgzMzI='}  # , 'submit' : 'Login'
    postdata = urllib.parse.urlencode(values).encode()
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    request = urllib.request.Request(LOGIN_URL, postdata, headers)
    try:
        response = opener.open(request)
        page = response.read().decode()
        # print(page)
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)

    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    # print(cookie)
    # for item in cookie:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)

    get_url = f'http://jwgl.qziedu.cn/jsxsd/framework/main_index_loadkb.jsp?rq={dayed}&sjmsValue=A3B9D58CF4AD4C97B59C1E0DEA2AB2B6'  # 利用cookie请求訪问还有一个网址
    get_request = urllib.request.Request(get_url, headers=headers)
    get_response = opener.open(get_request)
    # print(get_response.read().decode())
    total = []

    response = get_response.read().decode()
    text = response
    # text = response.text


    text1 = f'''<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta http-equiv="X-UA-Compatible" content="ie=edge" />

    <link rel="stylesheet" type="text/css" href="/jsxsd/assets/css/common.css" />

    <link rel="stylesheet" type="text/css" href="/jsxsd/assets/css/themes/edu-bg-balck.css" />
	<title>首页</title>
</head>

<style>
    
</style>
<body>
{text}
</body>
</html>
'''

    soup = BeautifulSoup(text1,'lxml')
    a_list = soup.select('.personal-table > thead > tr ' )
    a_list2 = soup.findAll('tbody')

    # print(a_list[0])
    # print(a_list2[0])
    text2 = f"{a_list[0]}" + f"\n{a_list2[0]}"
    # print(text2)
    text2 = f'''<html lang="en">
    <head>
    	<meta charset="UTF-8" />
    	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
    	<meta http-equiv="X-UA-Compatible" content="ie=edge" />

        <link rel="stylesheet" type="text/css" href="/jsxsd/assets/css/common.css" />

        <link rel="stylesheet" type="text/css" href="/jsxsd/assets/css/themes/edu-bg-balck.css" />
    	<title>首页</title>
    </head>

    <style>

    </style>
    <body>
    {text2}
    </body>
    </html>
    '''
    soup2 = BeautifulSoup(text2, 'lxml')
    # print(soup2)
    first_line = soup2.select('tr')

    first_line_ed = first_line[0].text.split()
    # print(len(first_line_ed))
    # print(first_line_ed)


    second_line = soup2.select('tbody > tr >td')
    text_line = soup2.select('tr')
    # print(text_line)
    # print("second_line:"+f'{second_line[0].text.split()}')
    # print(second_line[1])


    for i in range(0,43):
        if second_line[i].text.split() == []:
            total.append(["None"])
            continue
        original = str(second_line[i])
        # print(original)
        ex = '''上课地点：(.*?)">'''
        output1 = re.findall(ex,original,re.S)


        total.append(second_line[i].text.split()+output1)
        # total.append(second_line[i].text.split().append(output1[0]))

    # print(total)
    total_all = first_line_ed + total

    print(total_all)
    return total_all
    # print(second_line[42].text.split() == [])
    # print(second_line_1.split())


# def login():
#     url = "http://jwgl.qziedu.cn/jsxsd/xk/LoginToXk"
#     headers = {
#         'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
#         "Referer":"http://jwgl.qziedu.cn/jsxsd/",
#
#     }
#
#     data = {
#         "userAccount":"2003010533",
#         "userPassword":"Zhy13719218332",
#         "encoded":"MjAwMzAxMDUzMw%3D%3D%25%25%25Wmh5MTM3MTkyMTgzMzI%3D",
#     }
#     response = requests.post(url=url,headers=headers,data=data,allow_redirects=True)
#     print("login:"+ f"{response.status_code}")
#
#     _cookies  = response.cookies.items()
#     print(_cookies)
#     cookie = ''
#     for name, value in _cookies:
#         cookie += '{0}={1};'.format(name, value)
#     print(cookie)
#     return cookie
#     # _cookie = response.cookies
#     # print(_cookie)
#     # return _cookie

