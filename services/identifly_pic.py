import requests
import re

import pytesseract
from PIL import Image
from PIL import ImageEnhance

def get_url_identifly(msg,user_id,old_user_id):
    ex1 = r'url=([\s\S]*?)]'
    pic_url = re.findall(ex1, msg)
    if pic_url != [] and user_id == old_user_id:
        print(pic_url)
        return [True,pic_url[0]]
    return [False]

def identifly_pic(url):


    r = requests.get(url, stream=True)
    with open(r'F:\Sayotest2\sources\iden_pic.jpg', 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
        fd.close()


        # 读取图片
        im = Image.open('.\sources\iden_pic.jpg')
        im = im.convert('L')

        threshold = 120

        table = []

        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        im = im.point(table, '1')



        # 识别文字
        string = pytesseract.image_to_string(im, lang='chi_sim')

    return [True,string]

# import easyocr
# import requests
# import re
#
# def get_url_identifly(msg,user_id,old_user_id):
#     ex1 = r'url=([\s\S]*?)]'
#     pic_url = re.findall(ex1, msg)
#     if pic_url != [] and user_id == old_user_id:
#         print(pic_url)
#         return [True,pic_url[0]]
#     return [False]
#
# def identifly_pic(url):
#
#     r = requests.get(url, stream=True)
#     with open(r'F:\Sayotest2\sources\iden_pic.jpg', 'wb') as fd:
#         for chunk in r.iter_content():
#             fd.write(chunk)
#
#     reader = easyocr.Reader(['ch_sim', 'en'])
#     output = reader.readtext('F:\Sayotest2\sources\iden_pic.jpg')
#     str1 = ""
#     for i in output:
#         word = i[1]
#         str1 = str1 + word
#
#     return [True,str1]
