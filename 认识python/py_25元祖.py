#元祖
num_list = ("river",29,1.75,29)
print(num_list[1])

#定义一个只包含一个元素的元祖,需要在数据后加一个逗号
single_list = (5,)
print(single_list[0])

#取索引
print(num_list.index("river"))

#统计元素出现几次
print(num_list.count(29))

#统计长度
print(len(num_list))

