class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)

#创建猫对象
Tom = Cat()
#Tom.name = "Tom"
Tom.eat()
Tom.drink()
Tom.name = "Tom"
print(Tom)