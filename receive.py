import socket
import json

ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('127.0.0.1', 5710))
ListenSocket.listen(1000)

HttpResponseHeader = '''HTTP/1.1 200 OK
Content-Type: text/html
'''

#定位有效信息
def request_to_json(msg):
	for i in range(len(msg)):
		if msg[i]=="{" and msg[-1]=="}":
			return json.loads(msg[i:])
	return msg
	# return None

#需要循环执行，返回值为json格式
def rev_msg():# json or None
	conn, Address = ListenSocket.accept()
	Request = conn.recv(10240).decode(encoding='utf-8')
	#print(Request)
	rev_json=request_to_json(Request)
	#print(rev_json)
	conn.sendall((HttpResponseHeader).encode(encoding='utf-8'))
	conn.close()
	return rev_json