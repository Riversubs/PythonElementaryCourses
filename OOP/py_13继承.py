class Animal:

	def eat(self):
		print("吃")

	def drink(self):
		print("喝")

	def run(self):
		print("跑")

	def sleep(self):
		print("睡")


class Dog(Animal):

	def brak(self):
		print("汪汪叫")


class XiaoTianQuan(Dog):

	def fly(self):
		print("飞")

	#方法重写	
	def brak(self):
		#使用super调用父类的方法
		#super().brak()

		#早期版本调用父类方法:父类名.方法名(self)
		Dog.brak(self)

		print("神狗叫")

class Cat(Animal):

	def catch(self):
		print("抓老鼠")


#1.创建一个对象
wangcai = XiaoTianQuan()

#2.引用方法
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.brak()
wangcai.fly()

#3.创建猫对象
tom = Cat()

#4.引用方法
tom.eat()
tom.drink()
tom.run()
tom.sleep()
tom.catch()



