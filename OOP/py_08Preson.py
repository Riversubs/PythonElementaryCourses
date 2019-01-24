class Preson:

    def __init__(self,name,weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字是%s 体重是%.2f公斤" % (self.name,self.weight)

    def run(self):

        print("%s 爱跑步，跑步锻炼身体" % self.name)

        self.weight -= 0.5

    def eat(self):

        print("%s 是吃货，吃完这顿再减肥"% self.name)\

        self.weight += 1

#创建人类
xiaoming = Preson("小明",75.0)
xiaoming.run()
xiaoming.eat()



#输出小明
print(xiaoming)