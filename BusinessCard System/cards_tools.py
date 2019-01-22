#记录所有的名片字典
card_list = []

def show_menu():
	"""显示菜单"""
	print("*" * 50)
	print("欢迎使用【名片管理系统】V 1.0")	
	print("")
	print("1.新增名片")
	print("2.显示全部")
	print("3.查询名片")
	print("")
	print("0.退出系统")
	print("*" * 50)

def new_card():

	"""新增名片"""
	print("-" * 50)
	print("新增名片")

	# 1.提示用户输入名片的信息
	name_str = input("请输入姓名:")
	phone_str = input("请输入电话:")
	weixin_str = input("请输入微信:")
	email_str = input("请输入邮箱:")

	# 2.使用用户输入的名片信息建立字典
	card_dict = {"name":name_str,
				 "phone":phone_str,
				 "weixin":weixin_str,
				 "email":email_str}

	# 3.将名片字典添加到列表中
	card_list.append(card_dict)

	#print(card_list)

	# 4.提示用户添加成功
	print("添加成功!")

def show_all():

	"""显示所有名片"""
	print("-" * 50)
	print("显示所有名片")

	#判断是否存在数据
	if len(card_list) == 0:
		print("当期没有任何名片记录,请使用新增功能添加名片!")

		#返回函数执行结果,不会执行下方代码
		#如果return后面没有任何的内容,会返回到调用函数的未知,并且不返回任何结果
		return

	#打印表头
	for name in ["姓名","电话","微信","邮箱"]:
		print(name, end="\t\t")
	print(" ")

	#打印分割线
	print("=" * 52)

	#遍历列表
	for card_dict in card_list:
		print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],
									   card_dict["phone"],
									   card_dict["weixin"],
									   card_dict["email"]))

def search_card():

	"""搜索名片"""
	print("-" * 50)
	print("搜索名片")

	# 1.提示用户输入搜索的姓名
	find_name = input("请输入要查找的姓名: ")

	# 2.遍历列表查找用户姓名
	for card_dict in card_list:

		if card_dict["name"] == find_name :

			print("姓名\t\t电话\t\t微信\t\t邮箱")
			print("=" * 52)
			print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],
									   card_dict["phone"],
									   card_dict["weixin"],
									   card_dict["email"]))
			#修改删除名片
			deal_card(card_dict)
			break
	else:
		print("抱歉!没有找到 %s" % find_name)

def deal_card(find_dict):

	action_str = input("请输入要执行的操作:【1】修改,【2】删除,【0】返回上级菜单")

	if action_str == "1":

		find_dict["name"] = input_card_info(find_dict["name"] ,"姓名[回车不修改]:")
		find_dict["phone"] = input_card_info(find_dict["phone"],"电话[回车不修改]:")
		find_dict["weixin"] = input_card_info(find_dict["weixin"],"微信[回车不修改]:")
		find_dict["email"] = input_card_info(find_dict["email"],"邮箱[回车不修改]:")
		print("修改成功!")

	elif action_str == "2":
		card_list.remove(find_dict)
		print("删除成功!")

def input_card_info(dict_value,tip_message):

	#提示用户输入内容
	result_str = input(tip_message)

	#针对用户的输入进行判断
	if len(result_str) > 0:
		return result_str
	#如果用户输入了结果直接把结果返回
	#如果用户没有输入内容,返回字典中原有的值
	else:
		return dict_value