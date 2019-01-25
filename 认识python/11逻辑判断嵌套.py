has_ticket = False	
knife_length = 40

if has_ticket:
	print("车票检查通过,准备开始安检")
	if knife_length <= 20:
		print("安检成功,请进入车站")
	else:
		print("你携带的刀为%d公分!不允许进入车站!"%knife_length)
else:
	print("大哥,请先买票!")