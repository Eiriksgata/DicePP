HELP_STR = 'Dice++ by 梨子 Ver 0.2.2\n'
HELP_STR += '@骰娘 .bot on/off 开启或关闭骰娘\n'
HELP_STR += '.help指令 查看指令列表\n'
HELP_STR += '.help链接 查看源码地址\n'
HELP_STR += '.help协议 查看使用协议\n'
HELP_STR += '.help更新 查看最近更新内容与预告\n'
HELP_STR += '本骰娘的特色功能包括但不限于:优劣势投骰, 删除指定先攻条目, 记录生命值信息, 可部分匹配的查询功能\n'
HELP_STR += '交流群:861919492'

HELP_COMMAND_UPDATE_STR = '2020/3/2 本次更新内容:\n1.实装了暗骰功能\n2.实装了骰子表达式中的"抗性", "易伤"标记\n3.修改了今日人品的算法,更新了礼物池\n4.修复了一些错误\n\n'
HELP_COMMAND_UPDATE_STR += '下次更新预告:\n1.识别不友善行为与黑名单2.烹饪与点菜功能\n\n'
HELP_COMMAND_UPDATE_STR += '更多画饼请在交流群:861919492查看!'

HELP_COMMAND_STR = '多数指令需要后接参数, 主要指令包括:\n'
HELP_COMMAND_STR += '.bot 开关\n'
HELP_COMMAND_STR += '.r 掷骰\n'
HELP_COMMAND_STR += '.nn 设置昵称\n'
HELP_COMMAND_STR += '.ri 先攻\n'
HELP_COMMAND_STR += '.init 先攻列表\n'
HELP_COMMAND_STR += '.sethp 记录/调整生命值\n'
HELP_COMMAND_STR += '.jrrp 今日人品\n'
HELP_COMMAND_STR += '.查询 查询资料\n'
HELP_COMMAND_STR += '.dnd 初始属性作成\n'
HELP_COMMAND_STR += 'ps:骰娘会自动去掉大多数空格以及转换小写, 详细用法请输入.help[指令名]查询, 如.help r'

HELP_LINK_STR = 'Dice++是基于Python, NoneBot和酷Q的骰子机器人项目\n'
HELP_LINK_STR += '项目地址: https://github.com/haowen-li/DicePP'


HELP_AGREEMENT_STR =  '0.本协议是Dice++的服务协议。\n'
HELP_AGREEMENT_STR += '1.邀请骰娘, 使用掷骰服务和在群内阅读此协议视为同意并承诺遵守此协议，否则请移除骰娘。\n'
HELP_AGREEMENT_STR += '2.不允许禁言骰娘或刷屏掷骰等对骰娘的不友善行为，这些行为将会提高骰娘被制裁的风险。开关骰娘响应请使用.bot on/off。\n'
HELP_AGREEMENT_STR += '3.骰娘默认邀请行为已事先得到群内同意，因而会自动同意群邀请。因擅自邀请而使骰娘遭遇不友善行为时，邀请者因未履行预见义务而将承担连带责任。\n'
HELP_AGREEMENT_STR += '4.禁止将骰娘用于赌博及其他违法犯罪行为。\n'
HELP_AGREEMENT_STR += '5.对于设置敏感昵称等无法预见但有可能招致言论审查的行为，骰娘可能会出于自我保护而拒绝提供服务\n'
HELP_AGREEMENT_STR += '6.由于技术以及资金原因，无法保证骰娘100%的时间稳定运行，可能不定时停机维护或遭遇冻结，敬请谅解。\n'
HELP_AGREEMENT_STR += '7.对于违反协议的行为，骰娘将视情况终止对用户和所在群提供服务。\n'
HELP_AGREEMENT_STR += '8.本协议内容随时有可能改动。请注意帮助信息。\n'
HELP_AGREEMENT_STR += '9.Dice++参考了Dice! by 溯洄 Shiki的部分文字和指令设定, 但没有借鉴或复制任何代码, 如有疑问请联系qq:821480843。\n'
HELP_AGREEMENT_STR += '10.本服务最终解释权归服务提供方所有。'

HELP_COMMAND_R_STR =  '掷骰：.r[掷骰表达式]([掷骰原因]) [掷骰表达式]：([轮数]#)[个数]d面数(优/劣势)(k[取点数最大的骰子数])不带面数时视为掷一个默认的20面骰\n'
HELP_COMMAND_R_STR += '示例:\n'
HELP_COMMAND_R_STR += '.rd20+1d4+4\n'
HELP_COMMAND_R_STR += '.r4#d    //投4次d20\n'
HELP_COMMAND_R_STR += '.rd20劣势+4 //带劣势攻击\n'
HELP_COMMAND_R_STR += '.r2#d优势+4 攻击被束缚的地精 //两次有加值的优势攻击\n'
HELP_COMMAND_R_STR += '.r1d12+2d8+5抗性 //得到减半向下取整的投骰总值'

HELP_COMMAND_NN_STR =  '设置昵称：.nn [昵称]\n'
HELP_COMMAND_NN_STR += '私聊.nn视为操作全局昵称\n'
HELP_COMMAND_NN_STR += '优先级：群昵称>全局昵称>QQ昵称\n'
HELP_COMMAND_NN_STR += '示例:\n'
HELP_COMMAND_NN_STR += '.nn	//视为删除昵称\n'
HELP_COMMAND_NN_STR += '.nn dm //将昵称设置为dm'

HELP_COMMAND_RI_STR =  '加入先攻(群聊限定)：.ri([优劣势][加值]) ([名称])\n'
HELP_COMMAND_RI_STR += '示例:\n'
HELP_COMMAND_RI_STR += '.ri优势+1 //以昵称加入先攻列表\n'
HELP_COMMAND_RI_STR += '.ri20 地精 //将地精以固定先攻20加入先攻列表'

HELP_COMMAND_INIT_STR =  '显示先攻列表：.init ([可选指令]) [可选指令]:clr 清空先攻列表 del 删除指定先攻条目\n'
HELP_COMMAND_INIT_STR += 'del指令支持部分匹配\n'
HELP_COMMAND_INIT_STR += '示例:\n'
HELP_COMMAND_INIT_STR += '.init //查看先攻列表\n'
HELP_COMMAND_INIT_STR += '.init clr //清空先攻列表\n'
HELP_COMMAND_INIT_STR += '.init del 地精 //在先攻列表中删除地精'

HELP_COMMAND_QUERY_STR =  '查询资料: .查询 查询目标\n'
HELP_COMMAND_QUERY_STR += '查询指令支持部分匹配\n'
HELP_COMMAND_QUERY_STR += '目前可查询的内容有: 全拓展法术, 全拓展专长, DMG魔法物品(by花作噫), PHB与DMG生物(by花作噫), PHB工具(by赵小安), PHB武器与护甲(by邪恶)'

HELP_COMMAND_SETHP_STR =  '记录/调整生命值: .sethp ([调整目标])([符号]) [骰子表达式/数值](/[最大生命值])\n'
HELP_COMMAND_SETHP_STR += '生命值信息将在.init的结果中显示\n'
HELP_COMMAND_SETHP_STR += '不输入前置符号时默认为"="操作\n'
HELP_COMMAND_SETHP_STR += '不设置生命值则显示已损失生命值\n'
HELP_COMMAND_SETHP_STR += 'pc生命值信息与先攻列表独立\n'
HELP_COMMAND_SETHP_STR += '查询目标支持部分匹配先攻列表中的条目\n'
HELP_COMMAND_SETHP_STR += '注意dm用.ri [pc名字]将pc加入先攻列表时, 该条目不会和pc的生命值自动关联, 需要pc自己用.ri加入先攻列表\n'
HELP_COMMAND_SETHP_STR += '示例:\n'
HELP_COMMAND_SETHP_STR += '.sethp 地精- 1d12+2 // 对地精造成1d12+2点伤害\n'
HELP_COMMAND_SETHP_STR += '.sethp 20/30 // 将自己的生命值设置为20, 最大生命值设置为30\n'
HELP_COMMAND_SETHP_STR += '.sethp 杰+ 1d8+3 // 在先攻列表中匹配名字中有杰的对象, 然后给其增加1d8+3的生命值\n'
HELP_COMMAND_SETHP_STR += '.sethp // 删除自己的生命值信息'

HELP_COMMAND_JRRP_STR =  '这个指令也不清楚怎么用吗? #吃惊\n'
HELP_COMMAND_JRRP_STR += '.jrrp 查看今日人品'