import requests
import json
import re


def get_schedule():
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        'cookie':'JSESSIONID=C5595B8C7300BC8275FFB5C441BD5EB8; UM_distinctid=17718c323ff1fa-01b23d4de28f12-31346d-144000-17718c32400b8a; SERVERID=122; JSESSIONID=E5A07807665E2FC09417868A9435CA2B',

    }

    url = "http://jwgl.qziedu.cn/jsxsd/framework/main_index_loadkb.jsp?rq=2021-03-14&sjmsValue=A3B9D58CF4AD4C97B59C1E0DEA2AB2B6"

    total = []
    response = requests.get(url=url,headers=headers)
    text = response.text
    # print(response.status_code)
    # print(text)
    ex1 = r'''<th style="width: 10%;">(.*?)</th>'''
    line1 = re.findall(ex1,text,re.S)
    # print(line1[0])
    ex2 = r'''<th style="width: 12%;">(.*?)</th>'''
    line1_2 = re.findall(ex2, text, re.S)
    # print(line1_2)
    new_line1 = line1 + line1_2
    print(new_line1)
    ex3 = r'''<td>12\r\n\t\t\t\t<br>(.*?)\r\n\t\t\t\t<br/>(.*?)</td>'''
    line2_1 = re.findall(ex3, text, re.S)
    line2_1 = [line2_1[0][0]+'\n'+line2_1[0][1]]
    print(line2_1)

				

    
get_schedule()
