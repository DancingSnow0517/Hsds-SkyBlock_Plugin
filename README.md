# Hsds-SkyBlock_Plugin

一个[MCDReforged](https://github.com/Fallen-Breath/MCDReforged)插件

## 安装

需要一个新的MCDR解析器以支持玩家前缀

~~小天才魔改法~~

将``vanilla_parser_hsds.py``放入MCDR文件夹的``utils\parser``

将MCDR的``config.yml``的``parser``改为``vanilla_parser_hsds``

将插件``SkyBlock.py``放入``Plugin``文件夹

重载MCDR

### 数据包

将整文件夹``SkyBlock-Hsds``放入``world``的``datapack``文件夹

reload服务器

数据包修改了进度，引导玩家游玩，添加了一些懒人合成（见xk的数据包）

添加了9个线合成蜘蛛网，凋灵掉落下届合金碎片，末影人掉落末地石

在坐标X：-256 - 256 Y：0 - 256 Z：-256 - 256 会持续杀死除了玩家的任何生物，给予玩家饱和效果

## 配置

配置文件将会生成在``server/world/config``

### SkyBlock.json
```
{
    "player": {
        "DancingSnow": {
            "island": "1",
            "UUID": "212c5e19-8d74-473c-9a8c-520a8d93cca0"
        }
    },
    "pos": {
        "example": {
            "X": 10,
            "Y": 100,
            "Z": 1000,
            "statu": false,
            "color": "green"
        }
    }
}
```

``player``意思为目前拥有岛屿的玩家

``pos``用来储存岛屿信息

上面样例就是有拥有一个岛屿名为``example``，X，Y，Z的坐标，``statu``代表岛屿有没有被生成，``false``代表没有生成，当有玩家加入时将会生成一个拥有泥土，树苗和一个带有10个骨粉的箱子，``statu``将会变为``true``

``color``代表岛屿的颜色，将用于队伍的颜色

## 相关链接

[MCDR](https://github.com/Fallen-Breath/MCDReforged)用于加载插件

[Fabric](https://fabricmc.net/)用于加载Mods

[Carpet](https://www.curseforge.com/minecraft/mc-mods/carpet)SkyBlockMOD加载需要

[skyrising/skyblock](https://github.com/skyrising/skyblock/)用于生成虚空地形但保留结构群系和添加流浪商人配方

[BungeeCord](https://ci.md-5.net/job/BungeeCord/)蹦极端，用于盗版假人可加入

[Carpet-TIS-Addition](https://github.com/TISUnion/Carpet-TIS-Addition)用于自动给假人加上后缀``_bot``

[FabricProxy](https://www.curseforge.com/minecraft/mc-mods/fabricproxy/)链接BC段和fabric服务器


