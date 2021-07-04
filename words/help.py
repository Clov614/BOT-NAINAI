import json



def help_base():
    state = json.load(open("./state_pugins_data.json", encoding='utf-8'))
    help_base = f'''⭐帮助菜单 help_menu⭐:
        实现功能⭐blibli av bv 号 以及分享链接解析⭐
        指令如下:\n
        1.state:{state["weather_state"]}
        1.天气查询⭐对我说:天气 城市 详细（可选）
        2.state:{state["Anime_search_state"]}
        2.anime番剧搜索⭐对我说:找番（或者 番剧搜索）
        3.state:{state["pixiv_analysis_state"]}
        3.pixiv图片搜索⭐对我说:Pixiv图片检索
        4.state:{state["music_game_share_state"]}
        4.音游推荐⭐对我说:音游推荐
        5.state:{state["get_tu_state"]}
        5.随机loli库⭐对我说:车来
        6.state:{state["get_music_state"]}
        6.点歌⭐对我说:点歌 歌曲名
        7.基于学校官网的实时课表⭐对我说:课表 第几周
        8.state:{state["code_online_state"]}
        8.在线代码执行⭐对我说:执行代码 文件名(带后缀) 代码 input(可选)
        9.state:{state["automatic_state"]}
        9.自动化执行CQ码⭐对我说:自动化 CQ字段
        10.state:{state["pic_identifly_state"]}
        10.图片文字提取⭐对我说:提取文字(然后发出图片)
        11.state:{state["taobao_share_zk_state"]}
        11.淘宝优惠券⭐对我说:淘宝优惠券
        12.state:{state["taobao_share_zk_state"]}
        12.淘宝商品查询⭐对我说:商品查询 商品名
        13.state:{state["tackle_flash_state"]}
        13.⭐闪照提取⭐
        15.state:{state["tts_state"]}
        15.⭐文字转语音⭐对我说: tts 文字（tips:空格隔开）
        16.state:{state["cos_state"]}
        16.⭐随机cosplay⭐对我说: cosplay
        
        '''
    return help_base