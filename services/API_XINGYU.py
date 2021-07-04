import requests

def cosplay():
    url = "http://api.tianyi2006.xyz/api/cosplay.php"

    response = requests.get(url)
    text = response.text
    return text