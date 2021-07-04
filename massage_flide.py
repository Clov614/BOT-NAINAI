import json
from words import read_words
from send_message.send_message import send_message
from message_rules import talk_to_user
import random

self_qq = json.load(open("./config.json", encoding='utf-8'))["self_qq"]
at_msg = ["at我干嘛呢！","想要我告诉你使用方法请说help","干嘛！！","?"]
class msg_talker():
    def __init__(self):
        self.talk_data = read_words.read_file()    # talk_data即words.db中的语句，返回列表

    def private_msg(self,rev):
        if rev["sub_type"] != "friend":
            return send_message('你还不是我的好友呀', rev['user_id'], "private")
        return send_message(talk_to_user(rev, self.talk_data), rev["user_id"], "private")
    def group_msg(self, rev):
        send_this = talk_to_user(rev, self.talk_data)
        print(send_this)
        # if "[CQ:at,qq={}]".format(self_qq) in rev["raw_message"]:
        #     return send_message(random.choice(at_msg),rev["group_id"],"group")
        return send_message(send_this, rev["group_id"], "group")
