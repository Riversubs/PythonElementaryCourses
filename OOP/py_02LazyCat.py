class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")
#创建猫对象
Lazy_Cat = Cat()
Tom = Cat()

Tom.eat()
Tom.drink()

Lazy_Cat.eat()
Lazy_Cat.drink()

print(Lazy_Cat)
print(Tom)

Lazy_Cat2 = Lazy_Cat
print(Lazy_Cat2)