name_list = ["river", "czh", "chenzhihe"]

#取值
print(name_list[2])

#取索引
print(name_list.index("czh"))

#修改
name_list[0] = "lihuizhen"
print(name_list[0])

#增加数据
name_list.append("lhz")
print(name_list)

#插入数据
name_list.insert(1,"zh")
print(name_list)

#扩建列表
temo_list = ["孙悟空","猪八戒"]
name_list.extend(temo_list)
print(name_list)

#删除
name_list.remove("zh")
print(name_list)

#默认删除追后一个数据
name_list.pop()
print(name_list)

#删除指定数据
name_list.pop(0)
print(name_list)

del name_list[0]
print(name_list)

#列表长度统计
list_len = len(name_list)
print("列表后包含%d个元素" % list_len)

#列表计数
list_count = name_list.count("lhz")
print("lhz出现了%d次" % list_count)

#列表升序排序
num_list = [1,4,6,3,2,11,44,22,65,33]
#num_list.sort()
#print(num_list)

#列表降序
#num_list.sort(reverse=True)
#print(num_list)

#逆序
num_list.reverse()
print(num_list)

#清空列表
name_list.clear()
print(name_list)