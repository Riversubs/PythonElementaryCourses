#导入随机工具包(导入工具包的语句必须放在顶部,方便下方的代码引用工具包)
import random

#要求玩家从控制台输入要出的拳
player = int(input("请输出你您要出的拳,石头(1)/剪刀(2)/布(3):"))

#电脑随机出拳,先假定电脑只会出石头
computer = random.randint(1, 3)

print("玩家选择的拳头是%d - 电脑出的拳是%d" % (player,computer))

#判断玩家胜利的情况
if ((player == 1 and computer == 2) 
		or (player == 2 and computer == 3) 
		or (player == 3 and computer == 1)):

	print("玩家获胜!")
#判断平局
elif(player == computer):
	print("平局!")
#其他的情况就是电脑获胜
else:
	print("电脑获胜!")