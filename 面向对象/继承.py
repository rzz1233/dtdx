class Animal:
    def eat(self):
        print('eat')
    def sleep(self):
        print('sleep')
    def walk(self):
        print('walk')
class Dog(Animal):
    def bark(self):
        print('bark')
class xiaotianqian(Dog):
    def fly(self):
        print('fly')
    def sleep(self): #对父类方法的覆盖
        print('sleep1')
    def bark(self):
        super().bark()
        print('bark1')#对父类方法的扩展


dog = Dog()
xaio = xiaotianqian()
xaio.bark()
xaio.sleep()
dog.eat()