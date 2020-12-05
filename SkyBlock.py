import json,time,os,re

ConfigPath = 'server/world/config/'
LogPath = 'server/SkyBlockLogs/'

IslandLogs = ''
Message = ''
PlayerCD = {}

HelpMsg ='''§e使用§d!!island§r§e显示本条消息
§e使用§d!!island join§r§e加入岛屿
§e使用§d!!island back§r§e回到自己的岛屿
§e使用§d!!island leave§r§e退出岛屿
§e使用§d!!island status§r§e查看岛屿状态'''

def TimeToStr(t):
    S = t//3600
    F = (t - 3600*S)//60
    M = int(t - S*3600 - F*60)
    return '§e§l{}§r§d小时§e§l{}§r§d分钟§e§l{}§r§d秒'.format(int(S),int(F),int(M))

def GetUUID(server,name):
    with open('server/usercache.json','r') as f:
        Cache = json.load(f)
    for i in Cache:
        if i["name"] == name:
            return i["uuid"]

def CreatBlock(server,name):
    time.sleep(0.1)
    x = config["pos"][name]["X"] 
    y = config["pos"][name]["Y"]
    z = config["pos"][name]["Z"]
    server.execute('fill {0} {1} {2} {3} {4} {5} '.format(str(x+4),str(y-2),str(z+1),str(x-1),str(y),str(z-4)) + 'minecraft:dirt')
    server.execute('fill {} {} {} {} {} {}'.format(str(x+4),str(y-2),str(z-4),str(x+2),str(y),str(z-2)) + ' air')
    server.execute('setblock {} {} {}'.format(str(x),str(y),str(z)) + ' minecraft:bedrock')
    server.execute('fill {} {} {} {} {} {} minecraft:grass_block replace minecraft:dirt'.format(str(x-1),str(y),str(z+1),str(x+4),str(y),str(z-4)))
    server.execute('setblock {} {} {} minecraft:oak_sapling'.format(str(x),str(y+1),str(z-3)))
    server.execute('setblock {} {} {} minecraft:oak_sapling'.format(str(x+3),str(y+1),str(z)))
    server.execute('setblock {} {} {} minecraft:mycelium'.format(str(x+1),str(y),str(z-1)))
    server.execute('setblock {} {} {} minecraft:chest'.format(str(x+1),str(y+1),str(z-1)))
    server.execute('replaceitem block {} {} {} container.0 minecraft:bone_meal 10'.format(str(x+1),str(y+1),str(z-1)))



def JoinTeam(name,server):
    server.execute('team join {} {}'.format(config["player"][name]["island"],name))

def LeaveTeam(name,server):
    server.execute('team leave {}'.format(name))

def CreatTeam(server):
    for i in config["pos"]:
        server.execute('team remove ' + i)
        server.execute('team add ' + i)
        server.execute('team modify {} color {}'.format(i,config["pos"][i]["color"]))
        server.execute('team modify ' + i + ' prefix {"text":"[' + i + ']"}')

def SaveLog(server):
    Date = time.asctime(time.localtime(time.time())).split(' ')  
    Time = Date[3].split(':')
    if not os.path.exists('server/SkyBlockLogs'):
        os.mkdir('server/SkyBlockLogs')
        os.mkdir('server/SkyBlockLogs/Island')
        os.mkdir('server/SkyBlockLogs/Message')
    FileName = 'Message-{}-{}-{}-{}-{}-{}.txt'.format(Date[4],Date[1],Date[2],Time[0],Time[1],Time[2])
    with open(LogPath + 'Message/' + FileName,'w') as f:
        f.write(Message)
    FileName = 'IslandLog-{}-{}-{}-{}-{}-{}.txt'.format(Date[4],Date[1],Date[2],Time[0],Time[1],Time[2])
    with open(LogPath + 'Island/' + FileName,'w') as f:  
        f.write(IslandLogs)

def ReadConfig(server):
    global config
    global PlayerCD
    if not os.path.exists(ConfigPath):
        os.mkdir(ConfigPath)
    if os.path.exists(ConfigPath + 'SkyBlock.json'):
        with open(ConfigPath + 'SkyBlock.json','r') as f:
            config = json.load(f)
        with open(ConfigPath + 'PlayerCD.json','r') as f:
            PlayerCD = json.load(f)
    else:
        config = {}
        config["player"] = {}
        config["pos"] = {}
        PlayerCD = {}
        SaveConfig(server)
def SaveConfig(server):
    with open(ConfigPath + 'SkyBlock.json','w') as f:
        json.dump(config,f,indent=4)
    with open(ConfigPath + 'PlayerCD.json','w') as f:
        json.dump(PlayerCD,f,indent=4)
    ReadConfig(server)

def on_user_info(server,info):
    global IslandLogs
    global PlayerCD
    content = info.content
    player = info.player
    if content == '!!reload':
        ReadConfig(server)
        CreatTeam(server)
    if content == '!!seed':
        server.execute('tellraw ' + player + ' [{"text":"种子：[","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"-602119083159372943","color":"green","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"suggest_command","value":"-602119083159372943"},"hoverEvent":{"action":"show_text","value":"单击复制"}},{"text":"]","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
    if '!!island' in content:
        if len(content.split(' ')) == 1:
            server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island"},"hoverEvent":{"action":"show_text","value":"单击执行"} },{"text":"显示本条消息","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')     
            server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island join","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island join"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":"加入岛屿","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
            server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island back","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island back"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":"回到自己的岛屿","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
            server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island leave","color":"light_purple","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"退出岛屿(会清空背包，获得5小时CD！需要手动打命令)","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
            server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island status","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island status"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":"查看岛屿状态","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
            server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island spectator","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island spectator"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":"参观岛屿","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
            server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!seed","color":"green","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!seed"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":"获取种子","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
        else:
            if len(content.split(' ')) == 2:
                if content.split(' ')[1] == 'join':
                    server.execute('tellraw ' + player + ' [{"text":"目前现有岛屿如下：","color":"gold","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
                    for i in config["pos"]:
                        server.execute('tellraw ' + player + ' [{"text":"' + i + '","color":"gold","clickEvent":{"action":"run_command","value":"!!island join ' + i + '"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":" ' + '(X:' + str(config["pos"][i]["X"]) + ', Y:' + str(config["pos"][i]["Y"]) + ', Z:' + str(config["pos"][i]["Z"]) + ')","color":"aqua","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
                    server.tell(player,'§5单击名称快捷加入岛屿')
                if content.split(' ')[1] == 'leave':
                    if player in config["player"]:
                        del config["player"][player]  
                        PlayerCD[player] = time.time()
                        SaveConfig(server)
                        server.tell(player,'§4你已经没有岛屿了')
                        server.tell(player,'获得5小时冷却')
                        server.execute('tp ' + player + ' 0 101 0')
                        server.execute('gamemode adventure ' + player)
                        server.execute('clear ' + player)
                        server.execute('spawnpoint ' + player)
                        LeaveTeam(player,server)
                    else:
                        server.tell(player,'你本没有岛屿')    
                if content.split(' ')[1] == 'back':
                    if player in config["player"]:
                        server.tell(player,'§d3§b秒后传送！')
                        time.sleep(1)
                        server.tell(player,'§d2§b秒后传送！')
                        time.sleep(1)
                        server.tell(player,'§d1§b秒后传送！')
                        time.sleep(1)
                        server.execute('tp ' + player + ' {0} {1} {2}'.format(str(config["pos"][config["player"][player]["island"]]["X"]),str(config["pos"][config["player"][player]["island"]]["Y"] + 1),str(config["pos"][config["player"][player]["island"]]["Z"])))
                        server.execute('gamemode survival ' + player)
                        server.tell(player,'§b传送成功！')
                    else:
                        server.tell(player,'§c你还没有加入岛屿')
                        server.execute('tp ' + player + ' 0 101 0')
                        server.execute('gamemode adventure ' + player)
                if content.split(' ')[1] == 'status':
                    if player in config["player"]:
                        server.tell(player,'§a你已经加入了岛屿§d ' + config["player"][player]["island"])
                    else:
                        server.tell(player,'§c你还没有加入岛屿')
                    NameList = {}
                    for i in config["pos"]:
                        NameList[i] = ''
                    for i in config["player"]:
                        NameList[config["player"][i]["island"]] = NameList[config["player"][i]["island"]] + i + ','
                    for i in config["pos"]:
                        server.tell(player,'§d' + i + ':' + '§e' + NameList[i].rstrip(','))

                if content.split(' ')[1] == 'spectator':
                    server.execute('tellraw ' + player + ' [{"text":"目前现有岛屿如下：","color":"gold","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
                    for i in config["pos"]:
                        server.execute('tellraw ' + player + ' [{"text":"' + i + '","color":"gold","clickEvent":{"action":"run_command","value":"!!island spectator ' + i + '"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":" ' + '(X:' + str(config["pos"][i]["X"]) + ', Y:' + str(config["pos"][i]["Y"]) + ', Z:' + str(config["pos"][i]["Z"]) + ')","color":"aqua","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
                    server.tell(player,'§5单击名称快捷参观岛屿')                    
                
            else:
                if len(content.split(' ')) == 3:
                    if content.split(' ')[1] == 'join':
                        if player in config["player"]:
                            server.tell(player,'§a你已经加入岛屿了')
                        else:
                            if player in PlayerCD:
                                if time.time() - PlayerCD[player] < 18000:
                                    server.tell(player,'§d你还要' + TimeToStr(18000 - (time.time() - PlayerCD[player])) + '§r§d后才可以加入岛屿')
                                    return
                            if content.split(' ')[2] in config["pos"]:
                                IslandLogs = IslandLogs + '[{}]'.format(time.asctime(time.localtime(time.time()))) + player + ' 加入了岛屿 {}\n'.format(content.split(' ')[2])
                                config["player"][player] = {}
                                config["player"][player]["island"] = content.split(' ')[2]
                                config["player"][player]["UUID"] = GetUUID(server,player)
                                SaveConfig(server)
                                JoinTeam(player,server)
                                if content.split(' ')[2] in config["pos"]:
                                    server.execute('tp ' + player + ' {0} {1} {2}'.format(str(config["pos"][content.split(' ')[2]]["X"]),str(config["pos"][content.split(' ')[2]]["Y"] + 3),str(config["pos"][content.split(' ')[2]]["Z"])))
                                    server.execute('spawnpoint {} {} {} {}'.format(player,str(config["pos"][content.split(' ')[2]]["X"]),str(config["pos"][content.split(' ')[2]]["Y"] + 3),str(config["pos"][content.split(' ')[2]]["Z"])))
                                    server.execute('gamemode survival ' + player)
                                    server.execute('effect give ' + player + ' minecraft:regeneration 1 255')
                                    server.execute('effect give ' + player + ' minecraft:saturation 1 255')
                                    server.execute('clear ' + player)
                                    if config["pos"][content.split(' ')[2]]["statu"] == False:
                                        CreatBlock(server,content.split(' ')[2])
                                        config["pos"][content.split(' ')[2]]["statu"] = True
                                        SaveConfig(server)
                    if content.split(' ')[1] == 'spectator':
                        server.execute('tp ' + player + ' {} {} {}'.format(str(config["pos"][content.split(' ')[2]]["X"]),str(config["pos"][content.split(' ')[2]]["Y"] + 1),str(config["pos"][content.split(' ')[2]]["Z"])))
                        server.execute('gamemode spectator ' + player)
                        server.execute('tellraw ' + player + ' [{"text":"使用","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island back","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island back"},"hoverEvent":{"action":"show_text","value":"单击执行"}},{"text":"回到自己的岛屿","color":"yellow","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
                                

def on_load(server,old):
    ReadConfig(server)

def on_server_startup(server):
    ReadConfig(server)
    CreatTeam(server)
    for i in config["player"]:
        JoinTeam(i,server)

def on_player_joined(server,player):
    global Message
    if not ('_bot' in player):
        if player in config["player"]:
            server.execute('tellraw ' + player + ' {"text":"欢迎回来","color":"gold","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}')
            server.execute('tellraw '+ player + ' [{"text":"找不到你的岛屿？使用","color":"red","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island back","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island back"},"hoverEvent":{"action":"show_text","value":"单击执行"} },{"text":"回到你的岛屿","color":"red","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
        else:
            server.execute('/tellraw ' + player + ' [{"text":"你还没有加入任何岛屿，使用","color":"gold","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"!!island","color":"light_purple","bold":false,"italic":false,"underlined":true,"strikethrough":false,"obfuscated":false,"clickEvent":{"action":"run_command","value":"!!island"},"hoverEvent":{"action":"show_text","value":"单击执行"} },{"text":"查看更多信息","color":"gold","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
            server.execute('gamemode adventure ' + player)
            server.execute('tp ' + player + ' 0 101 0') 
            server.execute('spawnpoint ' + player)
        Message = Message + '[{}]'.format(time.asctime(time.localtime(time.time()))) + player + ' 加入了游戏\n'
def on_player_left(server, player):
    global Message
    Message = Message + '[{}]'.format(time.asctime(time.localtime(time.time()))) + player + ' 退出了游戏\n'