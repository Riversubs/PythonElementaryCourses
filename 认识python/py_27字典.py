#字典是一个无序的数据集合
xiaoming = {"name" : "小明",
			"gender" : True,
			"height" : 1.75}

#取值
print(xiaoming["name"])

#增加/修改
#如果Key存在,会修改Key对应的值,如果不存在,会新增键值对
xiaoming["age"] = 18
print(xiaoming)

xiaoming["age"] = 19
print(xiaoming)

#删除
xiaoming.pop("height")
print(xiaoming)

#统计键值对的数量
print(len(xiaoming))

#合并字典
#如果已经存在就键值对,会覆盖原有键值对
xiaoming2 = {"height":178,
			"age":20}
xiaoming.update(xiaoming2)
print(xiaoming)

#清空字典
xiaoming.clear()
print(xiaoming)