from receive import rev_msg
from send_message.send_message import send_message
import re
from services import blibli_analysis
from massage_flide import msg_talker
import datetime
talker = msg_talker()
print("start")

while True:
    try:
        rev = rev_msg()
        # print(rev)
        if rev == None:
            continue
    except:
        continue
    if rev["post_type"] == "message":
        print(rev)  # 需要功能自己DIY
        if rev["message_type"] == "private":  # 私聊
            talker.private_msg(rev)
        elif rev["message_type"] == "group":  # 群聊
            talker.group_msg(rev)
        else:
            continue
    elif rev["post_type"] == "notice":
        if rev["notice_type"] == "group_upload":  # 有人上传群文件
            continue
        elif rev["notice_type"] == "group_decrease":  # 群成员减少
            send_message(f'芜湖·有一位群友起飞了\n一路飞好吧....\n起飞的群友：{rev["user_id"]}\n起飞的时间：{datetime.datetime.fromtimestamp(rev["time"])}',rev['group_id'],'group')
            continue
        elif rev["notice_type"] == "group_increase":  # 群成员增加
            continue
        else:
            continue
    elif rev["post_type"] == "request":
        if rev["request_type"] == "friend":  # 添加好友请求
            pass
        if rev["request_type"] == "group":  # 加群请求
            pass
    else:  # rev["post_type"]=="meta_event":
        continue





    # if rev["post_type"] == "message":
    #     print(rev) #需要功能自己DIY
    #     # send_message(rev['message'],rev['group_id'],'group')
    # if re.search(ex_json,rev["message"]) != None:
    #     ex_url = r'qqdocurl":"(.*?)\?'
    #     this = re.findall(ex_url,rev["message"])
    #     MID = this[0].split('\\')
    #     url = ''
    #     for i in range(len(MID)):
    #         url = url + MID[i]
    #     # print(url)
    #     total_msg = blibli_analysis.blibli_get(url)
    #     send_message(total_msg,rev['group_id'],'group')


