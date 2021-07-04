import requests
import json
self_id = '2404504867'

def delete_msg(message_id):
	data = {
		'message_id':int(message_id),
	}
	recall_url = "http://127.0.0.1:5700/delete_msg"
	rev = requests.post(recall_url, data=data)



def set_group_whole_ban(group_id):
	data = {
		'group_id':int(group_id),
		'enable':'true',
	}
	url = "http://127.0.0.1:5700/set_group_whole_ban"
	rev = requests.post(url, data=data)

def unset_group_whole_ban(group_id):
	data = {
		'group_id':int(group_id),
		'enable':'false',
	}
	url = "http://127.0.0.1:5700/set_group_whole_ban"
	rev = requests.post(url, data=data)