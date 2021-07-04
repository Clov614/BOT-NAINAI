import requests


def music_get_163(music_name):
    url = 'http://music.163.com/api/search/pc'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    }


    params = {
        's':music_name,
        'offset':0,
        'limit':1,
        'type':1,
    }


    response = requests.post(url,headers,params=params)
    if response.status_code != 200:
        return [False]
    res_json = response.json()
    print(response.json())
    name = res_json['result']['songs'][0]['name']
    id = res_json['result']['songs'][0]['id']
    alias = res_json['result']['songs'][0]['alias']

    music_url = f'http://music.163.com/song/media/outer/url?id={id}.mp3'
    song_target_url = f'http://music.163.com/#/song?id={id}'


    return [True,name,id,alias,music_url,song_target_url]
