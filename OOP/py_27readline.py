#打开文件
file = open("py_26追加写入.py")

while True:
	#一次读取一行,避免内存压力过大
	text = file.readline()

	#判断是否读取到内容
	if not text:
		break

	print(text)

#文件关闭
file.close()