import requests
import re

def request_bli_id(bli_id):
    try:
        url = f"https://www.bilibili.com/video/{bli_id}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
        }
        response = requests.get(url=url, headers=headers)
        code = response.status_code
        if code != 200 :
            return [False]
        # print(response.text)
        text = response.text
        ex1 = r'<h1 title="(.*?)"'
        data_title = re.findall(ex1, text, re.S)
        # print(data_title[0])

        ex2 = '<span title="(.*?)"'
        data_total = re.findall(ex2, text, re.S)
        ex3 = r'itemprop="thumbnailUrl" content="(.*?)"'
        data_img = re.findall(ex3, text, re.S)
        # print(data_total)
        data_play = data_total[0]
        data_danmu = data_total[1]
        data_dianzan = data_total[2]
        data_coins = data_total[3]
        data_star = data_total[4]
        data_title = data_title[0]
        data_img = data_img[0]
        data_all = f"""blibli_share:\n标题：{data_title}\n[CQ:image,file={data_img}]
        {data_play}\n {data_danmu}\n {data_coins}\n
        {data_dianzan}\n  {data_star}\nurl: {url}\n\n >_<! 200 OK!!!
        """
    except IndexError:
        return [False]
        pass
    return [True,data_all]