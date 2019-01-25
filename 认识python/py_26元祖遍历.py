num_list = ("czh",2.1,3)

for my_list in num_list:
	#使用格式字符串拼接my_list,这个变量不方便
	#因为元祖中保存的数据类型一般是不同的
	print(my_list)


#格式化字符串后面的()本质上就是元祖
info_tuple = ("小明",18,1.95)
print("%s 年龄是 %d 身高是 %.2f" %("小明",18,1.95))

info_str = "%s 年龄是 %d 身高是 %.2f" %info_tuple
print(info_str)

#转换list为tuple
num_list = [1,2,3,4]
num_tuple = tuple(num_list)
print(type(num_tuple))

#转换元祖为list
num2_list = list(num_tuple)
print(type(num2_list))