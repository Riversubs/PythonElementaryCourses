#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cards_tools

#永远为真,不停的循环执行代码
while True:c
	#显示功能菜单
	cards_tools.show_menu()

	action_str = input("请选择希望执行的操作: ")
	print("你选择的操作是【 %s 】" % action_str)

	#1,2,3 执行名片的操作
	if action_str in ["1","2","3"]:
		#新增名片
		if action_str == "1":
			cards_tools.new_card()

		#显示全部
		elif action_str == "2":
			cards_tools.show_all()

		#查询名片
		elif action_str =="3":
			cards_tools.search_card()

	#0 退户系统
	elif action_str == "0":

		print("欢迎再次使用名片管理系统!")
		#退出无限循环
		break

	#其他内容提示输入错误
	else:

		print("输入不正确,请重新输入!")