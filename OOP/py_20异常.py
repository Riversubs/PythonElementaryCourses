try:
	#提示用户输入一个整数
	num = int(input("输入一个整数: "))

	#使用 8 除以用户输入的整数并输出
	result = 8 / num

	print (result)

#捕获值错误
except ValueError:
	print("请输入正确的整数")

#捕获未知错误
except Exception as result:
	print("未知错误 %s" % result)

else:
	print("尝试成功")

finally:
	print("无论是否错误,都执行这一句")