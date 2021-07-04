import requests
import re
import json


def picture_get(r18,keyword):
    url = 'https://api.lolicon.app/setu/'

    #'https://i.pixiv.cat/img-original/img/2018/11/12/00/06/21/71616630_p0.jpg'

    headers ={
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63',
         }
    params = {
        'r18':r18,
        # 'apikey':'52940238600e9235095d45',

    }
    if keyword != None:
        params['keyword'] = keyword
    response = requests.get(url=url,params=params,headers=headers)
    # print(response)
    text = response.json()
    target = []
    try:
        url_img = text['data'][0]['url']
        # count = text['quota']
        title = text['data'][0]['title']
        pid = text['data'][0]['pid']

        target.append(url_img)
        # target.append(count)
        target.append(title)
        target.append(pid)
    except Exception as e:
        try:
            target.append(str(text['code']))
            target.append(text['msg'])
        except Exception as e:
            pass


    return target     # [url,title,pid] 找不到为 [code,msg]

# s = picture_get()
# print(s)
