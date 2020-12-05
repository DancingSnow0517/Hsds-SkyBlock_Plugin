# Hsds-SkyBlock_Plugin

一个[MCDReforged](https://github.com/Fallen-Breath/MCDReforged)插件

## 安装

需要一个新的MCDR解析器以支持玩家前缀

~~小天才魔改法~~

将``vanilla_parser_hsds.py``放入MCDR文件夹的``utils\parser``

将MCDR的``config.yml``的``parser``改为``vanilla_parser_hsds``

将插件``SkyBlock.py``放入``Plugin``文件夹

重载MCDR

## 配置

配置文件将会生成在``server/world/config``

### SkyBlock.json

`{`

    `"player": {`

        `"DancingSnow": {`

            `"island": "1",`

            `"UUID": "212c5e19-8d74-473c-9a8c-520a8d93cca0"`

        `}`

    `},`

    `"pos": {`

        `"example": {`

            `"X": 10,`

            `"Y": 100,`

            `"Z": 1000,`

            `"statu": false,`

            `"color": "green"`

        `}`

    `}`
    
`}`

``player``意思为目前拥有岛屿的玩家

``pos``用来储存岛屿信息

上面样例就是有拥有一个岛屿名为``example``，X，Y，Z的坐标，``statu``代表岛屿有没有被生成，``false``代表没有生成，当有玩家加入时将会生成一个拥有泥土，树苗和一个带有10个骨粉的箱子，``statu``将会变为``true``

``color``代表岛屿的颜色，将用于队伍的颜色

## Mod支持

[Fabric | The home of the Fabric mod development toolchain. (fabricmc.net)](https://fabricmc.net/)用于加载Mods

[Carpet - Mods - Minecraft - CurseForge](https://www.curseforge.com/minecraft/mc-mods/carpet)SkyBlockMOD加载需要

[skyrising/skyblock: Minecraft mod for empty world generation and new ways to get certain items (github.com)](https://github.com/skyrising/skyblock/)用于生成虚空地形但保留结构群戏和添加流浪商人配方



