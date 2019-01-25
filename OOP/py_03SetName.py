class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)

#创建猫对象
Tom = Cat()
Tom.name = "Tom"
Tom.eat()
Tom.drink()
print(Tom)

#创建猫对象
Lazy_Cat = Cat()
Lazy_Cat.name = "大懒猫"
Lazy_Cat.eat()
Lazy_Cat.drink()
print(Lazy_Cat)