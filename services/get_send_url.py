import re
import requests
import socket
import time


def get_url(msg,user_id,group_id,old_user_id,old_group_id):
    ex1 = r'url=([\s\S]*?)]'
    pic_url = re.findall(ex1, msg)
    if pic_url != [] and user_id == old_user_id and group_id == old_group_id:
        return [True,pic_url]
    return [False]

def pa_request(pic_url):
    try:
        headers = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
        }
        
        socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
        requests.packages.urllib3.disable_warnings()  # 忽略警告
        # params['url'] = pic_url
        # API_url = 'https://saucenao.com/search.php'
        API_url = 'https://saucenao.com/search.php?url=' + pic_url[0]
        response = requests.get(url=API_url, headers=headers, verify=False)
        response.close()
        response.encoding = 'utf-8'
        page_text = response.text
        news = page_text
        ex = '>Pixiv #(.*?)</a><br'
        date1 = re.findall(ex, news, re.S)
        # print(date1[0])
        if date1 == []:
            date1 = ["None",1]
        ex2 = 'class="resulttitle"><strong>(.*?)</strong><br /></div><div'
        date2 = re.findall(ex2, news, re.S)
        # print(date2[0])
        if date2 == []:
            date2= ["None",1]
        ex3 = 'ID: </strong><a href="(.*?)" class='
        date3 = re.findall(ex3, news, re.S)
        # print(date3[0])
        if date3 == []:
            date3 = ["None",1]
            
        ex4 = 'raw-rating="1" src="(.*?)"'
        date4 = re.findall(ex4, news, re.S)
        # print(date4[0])
        if date4 == []:
            date4 = ["None",1]
        if date4[0][-4:] == ".gif":
            ex4a = 'raw-rating="3" src="(.*?)"'
            date4 = re.findall(ex4a,news,re.S)

        ex5 = '<div class="resultsimilarityinfo">(.*?)</div>'
        date5 = re.findall(ex5, news, re.S)
        # print(date5[0])
        totle = []
        totle.append(date1[0])
        totle.append(date2[0])
        totle.append(date3[0])
        totle.append(date4[0])
        totle.append(date5[0])
        if totle == ["None","None","None","None","None"]:
            return [True,"你是不是发错图了，我找不到！！！"]
        totle_all = f'''Name: {totle[1]}\nPixivID: {totle[0]}\nPixiv_url: {totle[2]}\n相似度： {totle[4]}\n''' + f"[CQ:image,file={totle[3]}]"
        print(totle_all)
    except Exception as e:
        print(e)
        return [True,"你是不是发错图了，我找不到！！！"]
        


    return [True,totle_all]
