import requests
import datetime
import re


def get_url_anime(msg,user_id,old_user_id):
    ex1 = r'url=([\s\S]*?)]'
    pic_url = re.findall(ex1, msg)
    if pic_url != [] and user_id == old_user_id:
        print(pic_url)
        return [True,pic_url[0]]
    return [False]

# def trace_moe(img_url):    # 旧API
#     try:
#         # img_url = 'http://gchat.qpic.cn/gchatpic_new/541982545/977906598-2363942415-319D1A56B5DEC9B31D09E28FC90C72CF/0?term=3'
#         # img_url = 'http://gchat.qpic.cn/gchatpic_new/541982545/3817463816-2801203299-884BB826404AE63A7D19C019F7708BAB/0?term=3'
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
#             "Content-Type": "application/json",
#         }
#         # url = f"https://trace.moe/api/search?url={img_url}"
#         url = f"https://api.trace.moe/search?anilistInfo&url={img_url}"
#
#         try:
#             response = requests.post(url, headers,timeout=9)
#
#         except requests.exceptions.ReadTimeout:
#             return [True,f'请求超时了呢（谨慎传入gif）']
#         # print(response.json())
#         json_res = response.json()
#         # print(json_res['docs'][0])
#
#         try:
#             dos = json_res['docs'][0]
#         except TypeError:
#             return [True, "你是不是发错图了，我找不到！！！"]
#         anilist_id = dos['anilist_id']
#         # print(anilist_id)
#         filename = dos['filename']
#         # print(filename)
#         at = dos['at']
#         # print(at)
#         tokenthumb = dos['tokenthumb']
#         # print(tokenthumb)
#
#         episode = dos['episode']    # 集数
#
#         target_url = f"https://trace.moe/preview.php?anilist_id={anilist_id}&file={filename}&t={at}&token={tokenthumb}"
#
#         response2 = requests.get(target_url, headers, allow_redirects=False)
#         if 'Location' in response2.headers.keys():  # 解决重定向
#             url = response2.headers.get('Location')
#
#         image_url = url.replace(url[24:29], 'image')
#
#         # video = requests.get(target_url,headers)
#         # with open('./sources/{}.mp4'.format(dos['anime']),'wb') as f:
#         #     f.write(video.content)
#         # print(target_url)   # 文件地址.mp4
#         #
#         # print(dos['from'])     # 开始时间
#         # print(dos['to'])        #  结束时间
#         # print(dos['similarity']) #  相似度
#         # print(dos['anime'])      # 番名
#         # print(dos['at'])        # 时刻
#
#         anime = dos['anime']
#         from_time = str(datetime.timedelta(seconds=dos['from']))
#         to_time = str(datetime.timedelta(seconds=dos['to']))
#         at_time = str(datetime.timedelta(seconds=dos['at']))
#         similarity = float(dos['similarity'])*100
#         # total_all = f'''搜索结果:\n番名:{anime}\n[CQ:video,file=./sources/{dos['anime']}.mp4]\n/start/:/{from_time}/\n/end/:/{to_time}/\n/图片时刻/:/{at_time}/\n相似度:{similarity}\npower by trace_moe！！'''
#
#         total_all = f'''搜索结果:\n番名:{anime}\n[CQ:image,file={image_url}]\n位置:第{episode}集\nStart:/{from_time}/\nEnd:/{to_time}/\n图片时刻:/{at_time}/\n相似度:{similarity}\npower by trace_moe！！'''
#
#         # print(total_all)
#     except IndexError or TypeError:
#         return [True, "你是不是发错图了，我找不到！！！"]
#         pass
#
#     return [True,total_all]


def trace_moe(img_url):
    try:
        headers = {
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
                     "Content-Type": "application/json",
                 }

        url = f"https://api.trace.moe/search?anilistInfo&url={img_url}"
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(f"response_error:"+e)
        result = data["result"][0]
        anilist = result["anilist"]
        title = anilist['title']['native']  # 标题
        romaji = anilist['title']['romaji']  # 罗马音
        english = anilist['title']['english']  # 英文
        episode = result['episode']  # 集数
        start = result['from']  # 开始时刻
        end = result['to']  # 结束时刻
        similarity = result['similarity']  # 相似度
        video = result['video']  # 视频
        image = result['image']  # 图片
        video_CQ = f"[CQ:video,file={video}]"
        total_all = f'''搜索结果:\n番名:{title}\n罗马音:{romaji}\nenglish:{english}\n[CQ:image,file={image}]\n位置:第{episode}集\nStart:/{start}/\nEnd:/{end}/\n图片时刻:/{start}/\n相似度:{similarity:.2f}\npower by trace_moe！！'''
    except Exception as e:
        return [True, f"一定是网不好，或者TX的锅XD\nerror:{e}"]
        pass

    return [True,total_all,video_CQ]