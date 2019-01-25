str = "HelloWorld"
print(str)

#长度
print(len(str))

#次数
print(str.count("l"))
print(str.count("abc"))

#位置
print(str.index("W"))
#子字符串不存在会报错,print(str.index("ABC"))

#判断是否只包含空格字符
print(str.isspace())

#判断字符串中是否只包含数字,无法判断特殊数字字符串
print(str.isdecimal())

#可以判断unicode字符串,\u00b2等
print(str.isdigit())

#可以判断unicode字符串,还可以判断中文数字
print(str.isnumeric())

#判断字符串开头
print(str.startswith("Hello"))

#判断结尾
print(str.endswith("d"))

#查找单词,如果自定的字符串不存在,会返回-1,index方法会报错
print(str.find("llo"))
print(str.find("abc"))

#替换replace执行完成后,会返回一个新的字符串,不会修改原来的字符串
print(str.replace("World","Python"))
print(str)

#文本对齐
poem = ["登鹳雀楼",
		"王之涣",
		"白日依山尽",
		"黄河入海流",
		"欲穷千里目",
		"更上一层楼"]
for poem_str in poem:
	#print(poem_str.center(20))
	#print(poem_str.rjust(10))
	print(poem_str.ljust(10))

#切片
num_str = "0123456789"
print(num_str[2:6])
print(num_str[2:])
print(num_str[:6])
print(num_str[:])
print(num_str[::2])
print(num_str[1::2])
print(num_str[2:-1])
print(num_str[-2:])
print(num_str[-1::-1])






