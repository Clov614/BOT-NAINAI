import requests
import json

def pixiv_rank():
    url = 'https://www.pixiv.net/ranking.php'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        
    }
    params = {
        'mode': 'daily',
        'content': 'illust',
        'p': '1',
        'format': 'json',
    }

    response = requests.get(url=url, headers=headers, params=params)
    json_data = response.json()

    title = []
    date = []
    tags = []
    url_total = []
    for i in range(0, 5):
        url = json_data['contents'][i]['url']
        new_url = "https://i.pixiv.cat/" + url[20:]
        url_total.append(new_url)
        title.append(json_data['contents'][i]['title'])
        date.append(json_data['contents'][i]['date'])
        tags.append(json_data['contents'][i]['tags'])

    total = f'''title:{title[0]}\ndate:{date[0]}\ntags:{tags[0]}\n[CQ:image,file={url_total[0]}]\n
title:{title[1]}\ndate:{date[1]}\ntags:{tags[1]}\n[CQ:image,file={url_total[1]}]\n
title:{title[2]}\ndate:{date[2]}\ntags:{tags[2]}\n[CQ:image,file={url_total[2]}]\n
title:{title[3]}\ndate:{date[3]}\ntags:{tags[3]}\n[CQ:image,file={url_total[3]}]\n
title:{title[4]}\ndate:{date[4]}\ntags:{tags[4]}\n[CQ:image,file={url_total[4]}]\n
'''
    return total