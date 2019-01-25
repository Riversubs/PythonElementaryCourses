# 1.输入苹果的单价
price = float(input("输入苹果的单价:"))

# 2.输入苹果的重量
weight = float(input("输入苹果的重量"))

# 3.计算苹果的价格
money = price * weight
 
# 4.输出苹果的价格
print("苹果的单价是:%f元/斤" %price)

# 格式化输出字符串
name = "小2明"
print("我的名字叫%s,请多多关照!" %name)

# 格式化输出整型,不到6位用0占位,超过6位该显示什么现实什么
student_no = 123
print("我的学号是%06d" % student_no)

#格式化输出小数.2控制小数点后的位数
price = 8.5
weight = 7.5
money = price * weight
print("苹果的单价是%.2f元/斤,购买了%.2f斤,需要支付%.2f元" %(price,weight,money))

scale = 0.25
print("数据的比例是%.2f%%" % (scale * 100))