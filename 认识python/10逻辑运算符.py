age = int(input("请输入你的年龄:"))
if age >= 0 and age <= 120:
	print("年龄输入正确!")
else:
	print("年龄输入错误!")

python_score = 20
c_score =20
if python_score >60 or c_score >60:
	print("考试通过!")
else:
	print("考试失败!")

is_employee = False
if not is_employee:
	print("请勿入内")

holiday_name = "春节"

if holiday_name == "平安夜":
	print("买苹果")
elif holiday_name == "情人节":
	print("买玫瑰")
elif holiday_name == "生日":
	print("买蛋糕")
else:
	print("今天不是节日")