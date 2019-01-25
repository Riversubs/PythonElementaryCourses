list = [1,2,3,4,2,4,2,2,3,4,5,6,8]
list2 = [1,3,4,2,4,5,6,3]

print(max(list))
print(min(list))
print(len(list))
del(list[1])
print(list)
print(list > list2)

list3 = [0,1,2]
list4 = [3,4,5]
#print(list3 + list4)
#print(list3 * list4)

a = "hello"
b = "python"
print(a + b)

list5 = [1]
list5.extend([2,3])
print(list5)

list6 = [2]
list6.append([7,9])
print(list6)

#成员运算符
list7 = [1,2,3,4,5,6,7,8,9,0]
print(3 in list7)
print(3 not in list7)

#只能判断字典的key
print("a" in {"a":"laowang"})
print("laowang" in {"a":"laowang"})

#完整for循环语法
list8 = [1,2,3,4,5,6,7,8,9]
for x in list8:
	print(x)
	if x == 2:
		break
else:
	print("没有找到2")
print("找到2,循环结束")

#for应用场景
students = [
			{"name":"阿A",
			 "age":18,
			 "gender":True,
			 "height":1.75,
			 "weight":50},
			 {"name":"阿B",
			 "age":19,
			 "gender":False,
			 "height":1.85,
			 "weight":60}
]

find_name = "阿C"

for stu_dict in students:

	print(stu_dict)

	if find_name == stu_dict["name"]:

		print("找到了 %s" % find_name)

		#如果已经找到应该直接退出循环
		break
else:
	#如果没有找到,给出提示
	print("没有找到 %s" % find_name)

print("循环结束")