i = 0
resule = 0

while i <= 100:
	#判断变量i是否是偶数
	if i % 2 ==0:
		resule += i
	i += 1

print("0-100之间的偶数累加=%d" % resule)