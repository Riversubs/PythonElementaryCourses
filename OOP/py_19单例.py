class MusicPlayer(object):

	instanc = None

	init_flag = False

	def __new__(cls,*args,**kwargs):

		#1.判断类属性是否为空对象
		if cls.instanc is None:
			
			#2.调用父类的方法为第一个对象分配空间
			cls.instanc = super().__new__(cls)

		#3.返回类属性保存的对象应用
		return cls.instanc


	def __init__(self):

		#1.判断是否执行过初始化动作
		if MusicPlayer.init_flag:
			return

		#2.如果没有执行过,执行初始化动作
		print("初始化播放器")

		#3.修改类属性的标记
		MusicPlayer.init_flag = True

#创建对象
player1 = MusicPlayer()
plarer2 = MusicPlayer()

print(player1)
print(plarer2)