from func_pugins import *
from words.base_talk import others_answer
from random import choice
from send_message import send_message
from services.get_send_url import get_url,pa_request
from services.trace_moe_api import get_url_anime,trace_moe
from services.identifly_pic import get_url_identifly,identifly_pic

def match(msg,talk_data):
	for row in talk_data:
		if row[0] in msg:
			return [True,row[1][0]]
	return [False,choice(others_answer["no_answer"])]

old_user_id = ''       #触发pixiv_analysis 后抓取的上一条消息的qq
old_group_id = ''
pixiv_state = 0        #判断是否需要抓图片的url
anime_state = 0
identi_pic_state = 0

def talk_to_user(rev,talk_data):
    global old_user_id,pixiv_state,anime_state,old_group_id,identi_pic_state


    msg = rev["message"]
    blibli_get = blibli_anayz(msg)

    msg = rev["raw_message"]
    # --------------------------------------------------------------------------------------帮助页面
    if_help = help_menu(msg)
    if if_help[0] == True:
        return if_help[1]
    # --------------------------------------------------------------------------------------删除数据
    if_del = del_data(msg, talk_data)
    if if_del[0] == True:
        return if_del[1]
    # --------------------------------------------------------------------------------------添加数据
    if_add = add_data(msg, talk_data)
    if if_add[0] == True:
        return if_add[1]
    if_add1 = add_data1(msg, talk_data)
    if match(msg, talk_data)[0] == True:
        return match(msg, talk_data)[1]
    if_reban = reban(msg, rev['user_id'])
    if if_reban[0] == True:
        return if_reban[1]
    try:
        if_setu = get_setu(msg,rev['user_id'],rev['time'],rev["group_id"])
        if if_setu[0] == True:
            return if_setu[1]
    except Exception as e:
        print(e)
        if_setu = get_setu(msg, rev['user_id'], rev['time'], rev["message_id"])
        if if_setu[0] == True:
            return if_setu[1]
    # --------------------------------------------------------------------------------------天气
    if_weather = weather(msg,rev['user_id'])
    if if_weather != None:
        return if_weather
    #--------------------------------------------------------------------------------pixiv排行榜
    if_pixiv_rank = get_pixiv_rank(msg)
    if if_pixiv_rank[0] == True:
        try:
            send_message.send_message("请稍后.......", rev["group_id"], "group")
        except Exception as e:
            send_message.send_message("请稍后.......", rev["user_id"], "private")
            pass
        return if_pixiv_rank[1]
    
    #----------------------------------------------------------------------------Pixiv图片检索
    if_pixiv_anal = pixiv_analysis(rev['message'],msg)   # 这边的Pixiv_analysis只负责判断消息是否符合
    if if_pixiv_anal[0] == True:
        pixiv_state = 1
        old_user_id = rev['user_id']
        try:
            old_group_id = rev['group_id']
        except Exception as e:
            print(e)
            old_group_id = old_user_id
            pass
        return if_pixiv_anal[1]
    if pixiv_state == 1 :

        try:
            results1 = get_url(rev['message'],rev['user_id'],rev["group_id"],old_user_id,old_group_id)
        except Exception :
            results1 = get_url(rev['message'], rev['user_id'], rev["user_id"], old_user_id, old_group_id)
        if results1[0] ==True:
            pixiv_state = 0
            try:
                send_message.send_message("请稍后.......",rev["group_id"],"group")
            except Exception as e:
                send_message.send_message("请稍后.......",rev["user_id"], "private")
                pass
            results = pa_request(results1[1])  # 这边的results为请求到的返回值

            return results[1]
    pixiv_state = 0
            # return "1122"
    #------------------------------------flash——img
    # if_flash_pic = flash_pic(msg)
    # if if_flash_pic[0] == True:
    #     return if_flash_pic[1]
    
    if_bli_share = av_bv_share(msg)
    if if_bli_share[0] == True:
        return if_bli_share[1]
    
    if_music_game_share = music_game_share(msg)
    if if_music_game_share[0] ==True:
        return if_music_game_share[1]

    
    if_anime_search = Anime_search(rev['message'])
    if if_anime_search[0] == True:
        anime_state = 1
        old_user_id = rev['user_id']
        return if_anime_search[1]
    if anime_state == 1:
        anime_state = 0
        results2 = get_url_anime(rev['message'], rev['user_id'], old_user_id)
        if results2[0] == True:
            try:
                send_message.send_message("请稍后.......", rev["group_id"], "group")
            except Exception as e:
                send_message.send_message("请稍后.......", rev["user_id"], "private")
                pass
            results_anime = trace_moe(results2[1])  # 这边的results为请求到的返回值  results2[1]为img_url
            try:
                send_message.send_message(results_anime[2],rev["group_id"], "group")
            except Exception as e:
                send_message.send_message(results_anime[2], rev["user_id"], "private")
            return results_anime[1]
    
    if_set_switch = set_switch(msg,rev['user_id'])
    if if_set_switch[0] == True:
        return if_set_switch[1]

    if_say_hellow = say_hellow(msg)
    if if_say_hellow[0] == True:
        return if_say_hellow[1]

    if_set_admin = set_admin(msg,rev['user_id'])
    if if_set_admin[0] == True:
        return if_set_admin[1]

    if_deadmin = deadmin(msg, rev['user_id'])
    if if_deadmin[0] == True:
        return if_deadmin[1]

    if_get_music = get_music(msg)
    if if_get_music[0] == True:
        return if_get_music[1]
    if_automatic = automatic(msg)
    if if_automatic[0] == True:
        return if_automatic[1]

    if_kebiao = kebiao(msg)
    if if_kebiao[0] == True:
        try:
            send_message.send_message("请稍后.......", rev["group_id"], "group")
        except Exception as e:
            send_message.send_message("请稍后.......", rev["user_id"], "private")
            pass
        return if_kebiao[1]

    if_code_online = code_onli(msg)
    if if_code_online[0] == True:
        return if_code_online[1]

    if_pycharm_setu = setu(msg)
    if if_pycharm_setu[0] == True:
        return if_pycharm_setu[1]

    if_check_identifly_pic = check_identifly_pic(rev['message'])
    if if_check_identifly_pic[0] == True:
        identi_pic_state = 1
        old_user_id = rev['user_id']
        return if_check_identifly_pic[1]
    if identi_pic_state == 1:
        identi_pic_state = 0
        pic_url = get_url_identifly(rev['message'], rev['user_id'], old_user_id)
        if pic_url[0] == True:
            try:
                send_message.send_message("请稍后.......", rev["group_id"], "group")
            except Exception as e:
                send_message.send_message("请稍后.......", rev["user_id"], "private")
                pass
            results_identifly = identifly_pic(pic_url[1])  # 这边的results为请求到的返回值  results2[1]为img_url
            return results_identifly[1]

    if_taobao_share_zk = taobao_share_zk(rev["message"])
    if if_taobao_share_zk[0] == True:
        final = if_taobao_share_zk[1]
        if isinstance(final,str):
            return final
        for i in final:
            Finishing = f"""复制到淘宝打开 \n{i[0]} \n[CQ:image,file={i[3]}] \n 优惠券:{i[1]} \n 券后价:{i[4]}"""
            try:
                send_message.send_message(Finishing, rev["group_id"], "group")
            except Exception as e:
                send_message.send_message(Finishing, rev["user_id"], "private")
                pass
        return "获取完成..."
    if_taobao_search = taobao_search(rev["message"])
    if if_taobao_search[0] == True:
        final = if_taobao_search[1]
        if isinstance(final,str):
            return final
        for i in final:
            Finishing = f"""复制到淘宝打开 \n{i[0]} \n[CQ:image,file={i[3]}] \n 优惠券:{i[1]} \n 券后价:{i[2]}"""
            try:
                send_message.send_message(Finishing, rev["group_id"], "group")
            except Exception as e:
                send_message.send_message(Finishing, rev["user_id"], "private")
                pass
        return "获取完成..."
    if_tackle_flash = tackle_flash(rev["message"])
    if if_tackle_flash[0] == True:
        try:
            tackle_send = if_tackle_flash[1]
            return tackle_send
        except Exception as e:
            pass

    if_tts = tts(rev["message"])
    if if_tts[0] == True:
        return if_tts[1]

    if dict(rev).get("group_id",1) != 1:
        msg_type = "group"
        if_recall = recall(rev["raw_message"])
    try:
        set_group_whole_ban(rev["message"],rev["group_id"])
        unset_group_whole_ban(rev["message"],rev["group_id"])
    except Exception:
        pass
    # cosplay API
    if_cosplay = cos(rev["message"])
    if if_cosplay[0] == True:
        cos_msg = f"[CQ:image,file={if_cosplay[1]}]"
        return cos_msg


    return blibli_get



