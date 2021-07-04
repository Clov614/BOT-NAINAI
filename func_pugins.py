import re
from services import blibli_analysis
from words.help import help_base
from services import picture_quest
from jieba import posseg
from services import get_weather
from services.bv_av_analize import request_bli_id
from check_states_decorater import check_state
import json
from services.music_get import music_get_163
from send_message import API_send
from services import PIL_Form,get_school_schedule
from taobao.API_taobao_tbk_dg_optimus_material import API_taobao_tbk_dg_optimus_material
from taobao.API_taobao_tbk_dg_material_optional import API_taobao_tbk_dg_material_optional
from services import API_XINGYU

admin_qq_list = json.load(open("./config.json", encoding='utf-8'))["admin_qq_list"]
config = json.load(open("./config.json", encoding='utf-8'))
write_groups = json.load(open("./config.json", encoding='utf-8'))["write_groups"]

def blibli_anayz(msg):
	try:
		ex_json = 'json,data=.*?'
		data = re.search(ex_json, msg)
		if data == None:
			return None
		else :
			ex_url = r'qqdocurl":"(.*?)\?'
			this = re.findall(ex_url, msg)
			MID = this[0].split('\\')
			url = ''
			for i in range(len(MID)):
				url = url + MID[i]
			total_msg = blibli_analysis.blibli_get(url)
			return total_msg	
	except IndexError:
		return None

def help_menu(msg):
	if msg == "help":
		return [True,help_base()]
	elif msg == "帮助":
		return [True,help_base()]
	else :
		return [False]

@check_state('add_data_state')
def add_data(msg,all_data):
	if msg.count("＋") != 1:
		return [False]
	if "/" in msg or "|" in msg:
		return [True,"不能含有/或|呀~"]
	if msg.split("＋")[1]=="":
		return [False]
	msg = msg.split("＋")
	if len(msg[0])< 3:
		return [True,"长度要大于2呀~"]
	for row in all_data:
		if msg[0] == row[0]:
			if msg[1] in row[1]:
				return [True,"这句话我已经会辣，不用再教我啦~"]
			row[1].append(msg[1])
			save_data(all_data)
			return [True,"添加成功！"]
	all_data.append([msg[0], [msg[1]]])
	save_data(all_data)
	return [True,"添加成功！"]

@check_state('add_data_state')
def add_data1(msg,all_data):    # 大小写都要兼容
	if msg.count("+") != 1:
		return [False]
	if "/" in msg or "|" in msg:
		return [True,"不能含有/或|呀~"]
	if msg.split("+")[1]=="":
		return [False]
	msg = msg.split("+")
	if len(msg[0])< 3:
		return [True,"长度要大于2呀~"]
	for row in all_data:
		if msg[0] == row[0]:
			if msg[1] in row[1]:
				return [True,"这句话我已经会辣，不用再教我啦~"]
			row[1].append(msg[1])
			save_data(all_data)
			return [True,"添加成功！"]
	all_data.append([msg[0], [msg[1]]])
	save_data(all_data)
	return [True,"添加成功！"]

def save_data(all_data):
	f1 = open("./words/words","w",encoding='UTF-8')
	for row in all_data:
		temp = row[0]+"|"+"".join([i+"/" for i in row[1]])
		f1.writelines(temp+"\n")
	f1.close()

@check_state('del_data_state')
def del_data(del_data,all_data):
	if del_data[:2] != "rm":
		return [False]
	msg = del_data[2:].split("＋")
	for i in range(len(all_data)):
		if msg[0] == all_data[i][0]:
			if len(all_data[i][1]) == 1:
				all_data.pop(i)
				save_data(all_data)
				return [True,"已经删除啦~"]
			all_data[i][1].remove(msg[1])
			save_data(all_data)
			return [True,"已经删除啦~"]
	return [True,"删除出错啦~"]

import last_message
@check_state('get_tu_state')
def get_setu(msg,user,time,group_id):
	# ---------------------------------------------------防恶意刷屏模块
	with open('./ban_id.db','r',encoding='utf-8') as a:
		ban_user = a.read().split(',')
		a.close()
	sta = last_message.last_message['time']
	# if (int(time) - int(sta)) <= 1 and user not in ban_user and user == last_message.last_message['user']:

	# 	ban_user.append(user)
	# 	# print(user)
	# 	print('ban_user:',ban_user)   # 打印被ban账号
	# 	total = ''
	# 	with open('./ban_id.db', 'w', encoding='utf-8') as c:
	# 		for i in ban_user:
	# 			total = total + str(i) + ','
	# 		c.write(total)
	# 		c.close()
	# # if str(user) in ban_user:       #-------------这两句话插入进功能，保证只有此功能被ban
	# # 	return [True,f"{user}You can't use this feature!!!"]
	# all_this = {
	# 	"user": user,
	# 	"time": time,
	# }
	# # print(type(all_this['time']))
	# last_message.last_message = all_this
	# -----------------------------------------------------以下才是功能
	r18 = '0'
	ex2 = ".*?r18.*?"
	state2 = re.search(ex2,msg)
	ex1 = '.*?(setu)|(车来).*?'
	ml = msg.split(" ",2)
	keyword = None
	if len(ml) == 3:
		keyword = ml[-1]
	if len(ml) == 2 and ml[-1] != "r18":
		keyword = ml[-1]


	state = re.search(ex1,msg)
	if state2 != None:
		r18 = '1'
	if state != None:
		if str(user) in ban_user:
			return [True, f"{user}You can't use this feature!!!"]
		#ban模块放入功能内
		if (int(time) - int(sta)) <= 1 and user not in ban_user and user == last_message.last_message['user']:

			ban_user.append(user)
			# print(user)
			print('ban_user:',ban_user)   # 打印被ban账号
			total = ''
			with open('./ban_id.db', 'w', encoding='utf-8') as c:
				for i in ban_user:
					total = total + str(i) + ','
				c.write(total)
				c.close()
		# if str(user) in ban_user:       #-------------这两句话插入进功能，保证只有此功能被ban
		# 	return [True,f"{user}You can't use this feature!!!"]
		all_this = {
			"user": user,
			"time": time,
			"group":group_id,
		}
		# print(type(all_this['time']))
		last_message.last_message = all_this
		try:
			if group_id not in write_groups: #限制非白名单群的图片格式
				target = picture_quest.picture_get(r18,keyword)  # [url,count,title,pid]
				if len(target) != 2:
					msged = "title:"+target[1]+"\n"+"pid:"+str(target[2])+"\n"+f"[CQ:image,type=flash,file="+target[0]+"]"
				else:
					msged = target[0] + target[1]
				return [True,msged]
				#这边下面是白名单群的
			target = picture_quest.picture_get(r18,keyword)
			if len(target) != 2:
				msged = "title:" + target[1] + "\n" + "pid:" + str(target[2]) + "\n" + f"[CQ:image,file=" + target[
						0] + "]"
			else:
				msged = target[0] + target[1]

			return [True,msged]
		except Exception as e:
			print(e)
			return [True, f"阿这，出了一点问题:{e}"]
	return [False]

global_weather_id = ''
@check_state('weather_state')
def weather(msg,weather_id):
	global global_weather_id
	try:
		if msg[:3] == "天气图":
			list_msg = msg.split(" ",1)
			city = list_msg[1]
			pic = get_weather.weather_get_pic(city)
			if pic[0] == 1:
				return f"[CQ:image,file={pic[1]}]"
			if pic[0] == 2:
				return pic[1]
	except Exception as e:
		return e
	for word1 in posseg.lcut(msg.strip()):

		if word1.flag =='ns' and global_weather_id == weather_id:
			global_weather_id = ''
			return get_weather.url_get(msg)
	if msg.strip() == "天气" or msg.strip() == "气温" or msg.strip() == "weather" or msg[:4]=="今天天气":
		global_weather_id = weather_id
		return "请问是什么城市？"

	if msg[:2] == "天气" or msg[:2] == "气温":
		last_msg = msg[3:]
		words = posseg.lcut(last_msg.strip())

		args = {
			'city':None,
			'is_detailed':None,
		}

		for word in words:
			if word.flag == 'ns':  # ns 表示该词为地名
				args['city'] = word.word
			elif word.word in ('详细', '报告', '详情'):
				args['is_detailed'] = True
		if args['city'] != None and args['is_detailed'] == True:
			return get_weather.url_get_details(args['city'])
		return get_weather.url_get(args['city'])

def reban(msg,user):   # 解除ban
	if msg[:5] =="reban" and user == 541982545:
		try:
			total = ''
			reban_id = msg[6:].strip()
			with open('./ban_id.db', 'r+', encoding='utf-8') as a:
				ban_user = a.read().split(',')
				ban_user.remove(reban_id)
				a.close()

			for i in ban_user:
				total = total+str(i)+','
			with open('./ban_id.db', 'w', encoding='utf-8') as b:
				b.write(total)
				b.close()

			return [True,"成功reban!!!"]
		except ValueError:
			return [True,"语法错误！！"]
			pass

	return [False]

@check_state('pixiv_analysis_state')
def pixiv_analysis(msg,raw_msg):
	ex1 = r'url=([\s\S]*?)]'
	if raw_msg[:9] == 'Pixiv图片检索' or raw_msg[:9] == 'pixiv图片检索':
		return [True,'请发出图片']
	if raw_msg[:1] == 'p' or raw_msg[:1] == 'P':
		return [True,'Pixiv图片检索?']
	if raw_msg[:3] == '查图片' or raw_msg[:2] =="pa":
		return [True, '请发出图片']
	return [False]

# def flash_pic(msg):
# 	ex1 = r'\[CQ:image,type=flash,file=(.*?)]'
# 	push = re.findall(ex1, msg)
# 	if push != []:
# 		return [True,f"[CQ:image,file={push}]"]
# 	return [False]
@check_state('av_bv_share_state')
def av_bv_share(msg):
	if msg[:2] =='av' or msg[:2] =='bv' or msg[:2] =='AV' or msg[:2] =='BV':
		if len(msg) ==2:
			return [False]

		data_all = request_bli_id(msg)
		if data_all[0] == True:
			return [True,data_all[1]]

	return [False]

@check_state('music_game_share_state')
def music_game_share(msg):
	if msg[:4] == '音游推荐':
		music_game_list = '''Sonolus/一款（bangdream）邦邦模拟器/:https://tool.sonolus.reikohaku.fun/quick-start\n
		Project_Sekai/世界计画 多彩舞台！feat. 初音未来/:https://konmai.cn/\n
		Arcaea/上下轨道音游（有分天空轨）/:https://konmai.cn/#arcaea \n
		BanG Dream!/养成类音游(难度偏简单)/:https://konmai.cn/#bang-dream-girls-band-party\n
		D4DJ Groovy Mix/类bangdream/:https://konmai.cn/#d4dj-groovy-mix\n
		Phigros/强烈推荐，音乐好听，节奏带感,颇具创意/:https://konmai.cn/#phigros\n
		cytusⅡ/taptap有的下载/\n
		未完待补全.......

		'''
		return [True,music_game_list]

	return [False]

@check_state('Anime_search_state')
def Anime_search(msg):
	if msg[:4] == '番剧搜索' or msg[:2] == '找番':
		return [True, '请发出图片']
	if msg[:5] == 'anime' or msg[:1] == 'a':
		return [True, 'anime番剧搜索?']
	if msg[:3] == 'search':
		return [True, 'anime番剧搜索?']
	return [False]

def set_switch(msg,user):
	global state_pugins
	if (msg == 'set' or msg == '设置') and user in admin_qq_list:
		set_help = """   设置帮助:   \n格式: set function on(off)\n funcs:\nadd_data(添加词汇)
		\ndel_data(删除词汇)\nget_**tu(你说啥？)\nweather(查询天气)\npixiv_analysis(pixiv图片检索)\nav_bv_share(av bv号解析)
		\nmusic_game_share（音游分享）
		\nAnime_search(番剧搜索)
		\nget_music（歌曲分享）
		\nkebiao（基于学校官网的在线课表）
		\nautomatic(自动化执行CQ码)
		\ncode_online(在线执行代码)
		\npic_identifly(图片文字提取)
		\ntackle_flash(闪照提取)
		\ntts(文字转语音)
		\ncos(cosplay图片)
		"""
		return [True,set_help]
	if msg[:3] == 'set' and user in admin_qq_list:
		try :
			mid_msg = msg[4:].split(' ')
			# print(mid_msg)
			fuc_name = mid_msg[0]
			switch = mid_msg[1]

		except Exception as e:
			print(e)
			return [True,'语法错误']

		funcname = fuc_name+"_state"
		print(funcname)
		if switch == 'on':
			state_pugins = json.load(open("./state_pugins_data.json", encoding='utf-8'))
			state_pugins[funcname]="on"
			unwrited = json.dumps(state_pugins)
			with open("./state_pugins_data.json",'w' ,encoding='utf-8') as f:
				f.write(unwrited)
			return [True,f'set successfully!!!']
		if switch == 'off':
			state_pugins = json.load(open("./state_pugins_data.json", encoding='utf-8'))
			state_pugins[funcname]="off"
			unwrited = json.dumps(state_pugins)
			with open("./state_pugins_data.json",'w' ,encoding='utf-8') as f:
				f.write(unwrited)
			return [True, 'set successfully!!!']


	return [False]


def say_hellow(msg):
	if msg == 'sayo' or msg == 'Sayo':
		return [True,'在呢，详细指令请说help']

	return [False]

def set_admin(msg,user):
	global config,admin_qq_list
	if msg[:8] =="setadmin" and user == 541982545:
		list1 = msg.split(" ")
		try:

			set_user = int(list1[1])
			if set_user not in admin_qq_list:
				admin_qq_list.append(set_user)
			print(admin_qq_list)
			config["admin_qq_list"] = admin_qq_list
			with open("./config.json",'w', encoding='utf-8') as f:
				f.write(json.dumps(config))
				f.close()
			return [True,f"成功设置{set_user}为管理员!!!"]
		except ValueError or IndexError as e:
			print(ValueError)
			return [True,"语法错误！！"]
			pass
	return [False]


def deadmin(msg,user):
	global config, admin_qq_list
	if msg[:7] == "deadmin" and user == 541982545 and len(msg)>=9:
		list1 = msg.split(" ")
		try:

			rm_user = int(list1[1])
			if rm_user in admin_qq_list:
				admin_qq_list.remove(rm_user)
			else:
				return [True,"找不到该id"]
			print(admin_qq_list)
			config["admin_qq_list"] = admin_qq_list
			with open("./config.json", 'w', encoding='utf-8') as f:
				f.write(json.dumps(config))
				f.close()
			return [True, f"成功移除{rm_user}的管理员权限!!!"]
		except ValueError or IndexError:
			print(ValueError)
			return [True,"语法错误！！"]
			pass
	return [False]

@check_state("get_music_state")
def get_music(msg):
	if msg[:2] == '点歌' or msg[:5] == 'music' :
		list1 = msg.split(' ',1)
		try:
			music_name = list1[1]
			total = music_get_163(music_name)
			if total[0] == True :
				send_all = f'''[CQ:music,type=custom,url={total[5]},audio={total[4]},title={total[1]}]'''
				return [True,send_all]
		except Exception as e:
			print(e)
			return [True,'语法错误！！']

	return [False]

from services.pixiv_rank import pixiv_rank
@check_state("pixiv_rank_state")
def get_pixiv_rank(msg):
	if msg == "pixiv排行榜" or msg == "p站排行榜" or msg == "P站排行榜" or msg == "插画排行榜" or msg == "pixiv rank":
		try:
			total = pixiv_rank()
			return [True,total]
		except Exception as e:
			return [True,e]

	return [False]
@check_state("automatic_state")
def automatic(msg):
	try:
		if msg[:3] == "自动化" or msg[:4] == "auto":
			middle = msg.split(" ",1)
			target = middle[1]
			total = r"{}".format(target).replace("&#91;","[").replace("&#93;","]")
			# total = r"{}".format(target)
			return [True,total]
	except Exception as e :
		print(e)
		return [True,"语法错误哦！"]
	return [False]

@check_state("kebiao_state")
def kebiao(msg):
	if msg[:2] == "课表":
		try:
			middle = msg.split(" ",1)
			give_day = middle[1]
			total = get_school_schedule.get_schedule(give_day)
			PIL_Form.schedule_img(total)
			return [True,"注意：英语课教室请勿参考，后面带的参数为周次"+r"[CQ:image,file=file:///F:\Sayotest2\sources\new.jpg]"]
		except Exception as e:
			return [True,e]

	return [False]

from services.code_online import code_online

@check_state("code_online_state")
def code_onli(msg):
	if msg[:4] == "执行代码" or msg[:6] == "coding":
		try:
			middle = msg.split(" ",2)
			# 执行代码 文件名 code input
			name = middle[1]
			code = middle[2]
			data_json = code_online(name,code)
			return [True, f'''stdout: {data_json['stdout']}\nerror: {data_json['error']}\nstderr: {data_json['stderr']}''']
		except Exception as e:

			return [True,e]

	return [False]

def setu(msg):
	ex = ".*?色图.*?"
	search = re.search(ex,msg)
	if search != None:
		return [True,r"[CQ:image,file=file:///F:\Sayotest2\sources\setu.jpg]"]

	return [False]

@check_state("pic_identifly_state")
def check_identifly_pic(msg):
	if msg == "图片识别" or msg == "提取文字" or msg == "提取图片文字" or msg == "文字提取"\
			or msg == "文字识别" or msg == "识别文字":
		return [True,"请发出图片"]

	return [False]

@check_state("taobao_share_zk_state")
def taobao_share_zk(msg):
	if msg == "淘宝优惠券" or msg == "淘宝券" :
		try:
			final = API_taobao_tbk_dg_optimus_material()
		except Exception :
			try:
				final = API_taobao_tbk_dg_optimus_material()
			except Exception :
				return [True,"发生了一点错误，请重试"]
		return [True,final]

	return [False]

@check_state("taobao_search_state")
def taobao_search(msg):

	try:
		msg = msg.split(" ",1)
		if msg[0] == "商品查询" or msg[0] == "淘宝商品查询" or msg[0] == "优惠查询":

			final = API_taobao_tbk_dg_material_optional(msg[1])

			return [True,final]



	except Exception as e:
		return [True,e]

	return [False]

@check_state("tackle_flash_state")
def tackle_flash(msg):

	ex = "type=([\S\s]*?)"
	state = re.search(ex,msg)   #假如找不到则为None
	# text = "[CQ:image,type=flash,file=0b277ccdb93eaba10f0d5ddc4a3adffe.image]"
	ex2 = "file=([\S\s]*?).image"
	if state != None:
		MD5_get = re.findall(ex2,msg)
		MD5_get_up = str(MD5_get[0]).upper()
		tackle_url = f"https://gchat.qpic.cn/gchatpic_new/0/-0-{MD5_get_up}/0"
		tackle_send = f"[CQ:image,file={tackle_url}]"
		return [True,tackle_send]

	return [False]

@check_state("tts_state")
def tts(msg):
	try:
		msg = msg.split(" ",1)
		if msg[0] == "tts" or msg[0] == "文字转语音":
			tackle_send = f"[CQ:tts,text={msg[1]}]"
			return [True,tackle_send]
	except Exception as e:
		return [True,e]

	return [False]


def recall(msg):


	ex = "id=(.*?)]"
	ex1 = "qq=(.*?)]"
	L_msg = msg.split(" ",2)
	msg_front = re.findall(ex,L_msg[0])
	# print(msg_front)
	try:
		recall_id = msg_front[0]
	except Exception:
		pass

	if L_msg[-1] == "撤回" or L_msg[-1] == "recall":
		API_send.delete_msg(message_id=recall_id)



	return [False]

def set_group_whole_ban(msg,group):
	if msg == "全体禁言" or msg == "全员禁言":
			API_send.set_group_whole_ban(group)

def unset_group_whole_ban(msg,group):
	if msg == "解除全体禁言" or msg == "解除全员禁言":
			API_send.unset_group_whole_ban(group)

@check_state("cos_state")
def cos(msg):
	if msg == "cos" or msg == "cosplay":
		cos_url = API_XINGYU.cosplay()
		return [True,cos_url]
	ex1 = '三次元'
	state = re.search(ex1,msg)
	if state != None:
		cos_url = API_XINGYU.cosplay()
		return [True, cos_url]

	return [False]

