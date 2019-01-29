class A:

	def test(self):
		print("test")

class B:

	def demo(self):
		print("B_demo")

#多继承
class C(A,B):

	pass


#创建对象
c = C()

#调用父类方法
c.test()
c.demo()