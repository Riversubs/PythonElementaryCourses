#从某个模块中导入某个工具
from py_01Cat import Cat

#创建猫对象
tom = Cat()

tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%x" % addr)
