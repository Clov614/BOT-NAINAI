import requests



def url_get(city):
    url = f"https://wttr.in/{city}?format=1"
    res = requests.get(url=url,headers={ 'User-Agent': 'box-s-ville.Sayobot' })
    return res.text

def url_get_details(city):
    _format = (
        '%l:\n'
        '+%c+%C:+%t\n'
        '+💦+Humidity:+%h\n'
        '+💧+Precipitation:+%p\n'
        '+🍃+Wind:+%w'
    )
    url = f'https://wttr.in/{city}?format={_format}'
    res = requests.get(url=url,headers={ 'User-Agent': 'box-s-ville.Sayobot' })
    return res.text

def weather_get_pic(city):
    pic_url = f'https://v3.wttr.in/v3/{city}.png'
    response = requests.get(pic_url)
    code = response.status_code
    if code != 200 :
        return [2,f"state_code: {code}"]

    return [1,pic_url]