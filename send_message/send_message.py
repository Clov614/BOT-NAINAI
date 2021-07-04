import requests
import json

def send_message(msg,qq_id,qq_type):
	if qq_type == "private":
		data = {
			'user_id':qq_id,
			'message':msg,
			'auto_escape':False
		}
		cq_url = "http://127.0.0.1:5700/send_private_msg"
		rev = requests.post(cq_url,data=data)
	elif qq_type == "group":
		data = {
			'group_id':qq_id,
			'message':msg,
			'auto_escape':False
		}
		cq_url = "http://127.0.0.1:5700/send_group_msg"
		rev = requests.post(cq_url,data=data)
	else:
		return False
	if rev.json()['status'] == 'ok':
		return True
	return False


# def send_message(msg,qq_id,qq_type):
#
# from websocket_server import WebsocketServer
# import json
#
#
# class CqServer(object):
# 	def __init__(self):
# 		self.server = WebsocketServer(port=8765, host="localhost")
#
# 		self.server.set_fn_new_client(self.new_client)
# 		self.server.set_fn_client_left(self.client_left)
# 		self.server.set_fn_message_received(self.message_received)
#
# 		self.server.run_forever()
#
# 	def new_client(self, client, server):
# 		print(
# 			"New Client Join.\nIP : {}\nID : {}\n".format(client["address"], client["id"])
# 		)
#
# 	def client_left(self, client, server):
# 		print("Client Leave.\nIP : {}\nID : {}\n".format(client["address"], client["id"]))
#
# 	def message_received(self, client, server, message):
# 		print(message)
# 		data = {
# 				  "action": "send_private_msg",
# 				  "params": {"user_id":"541982545", "message": "Hello World!"},
# 		}
# 		server.send_message(client,bytes(json.dumps(data).encode("utf-8")))
#
