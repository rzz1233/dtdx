# 1. 按照以下要求定义一个游乐园门票类，并创建实例调用函数，完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
# 1)平日票价100元，2)周末票价为平日票价120%，3)儿童半价
# class Ticket(object):
#     def __init__(self):
#         self.price1 = 100
#         self.price2 = self.price1*1.2
#     def pingri(self):
#         self.sum_price = self.num1*self.price1 + self.num2*(self.price1/2)
#         print(f"总票价为：{self.sum_price}")
#     def zhoumo(self):
#         self.sum_price = self.num1 * self.price2 + self.num2 * (self.price2/2)
#         print(f"总票价为：{self.sum_price}")
#     def main(self):
#         self.time = int(input("请输入周几："))
#         self.num1 = int(input("请输入成人人数："))
#         self.num2 = int(input("请输入儿童人数："))
#         if self.time >0 and self.time <=5:
#             self.pingri()
#         elif self.time >5 and self.time <= 7:
#             self.zhoumo()
#         else:
#             print("时间输入错误")
# ticket = Ticket()
# ticket.main()

# 2.按以下要求定义一个乌龟类和鱼类并尝试编写游戏
# 假设游戏场景范围(x,y)为0<=x<=10,0<=y<=10;
# 游戏生成1只乌龟和10条鱼；
# 它们的移动方向均随机；
# 乌龟最大移动能力是2（它可以随机选择1还是2移动），鱼儿最大移动能力是1；
# 当移动到场景边缘，自动向反方向移动；
# 乌龟初始化体力为100（上限）；
# 乌龟每移动一次，体力消耗1；
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20；
# 鱼暂不计算体力；
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0时游戏结束
import random
class wugui(object):
    def __init__(self):
        self.tili = 100  
        self.x = random.randint(0, 10)  
        self.y = random.randint(0, 10)  
    def move(self):
        # 随机选择移动1或2步
        lis1 = [1,2]
        move1 = random.choice(lis1)
        # 随机选择移动的方向
        lis2 = ["up", "down", "left", "right"]
        direction = random.choice(lis2)
        if direction == "up":
            self.y += move1
        elif direction == "down":
            self.y -= move1
        elif direction == "left":
            self.x -= move1
        elif direction == "right":
            self.x += move1
        # 到边界的情况
        if self.x < 0:
            self.x = 0
        elif self.x > 10:
            self.x = 10
        if self.y < 0:
            self.y = 0
        elif self.y > 10:
            self.y = 10
        # 体力消耗1
        self.tili -= 1
        return (self.x, self.y)
    def eat(self):
        self.tili += 20
        if self.tili > 100:
            self.tili = 100

class Fish(object):
    def __init__(self):
        self.x = random.randint(0, 10)  # 初始化鱼的随机初始x坐标
        self.y = random.randint(0, 10)  # 初始化鱼的随机初始y坐标

    def move(self):
        move2 = 1
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            self.y += move2
        elif direction == "down":
            self.y -= move2
        elif direction == "left":
            self.x -= move2
        elif direction == "right":
            self.x += move2
        if self.x < 0:
            self.x = 0
        elif self.x > 10:
            self.x = 10
        if self.y < 0:
            self.y = 0
        elif self.y > 10:
            self.y = 10
        return (self.x, self.y)
class View(object):
    def main(self):
        Wugui = wugui()
        fish_lis = [Fish(), Fish(), Fish(), Fish(), Fish(), Fish(), Fish(), Fish(), Fish(), Fish()]

        while True:
            if Wugui.tili <= 0 or len(fish_lis) == 0:
                break
            Wugui_position = Wugui.move()

            for fish in fish_lis:
                fish_position = fish.move()
                if fish_position == Wugui_position:
                    fish_lis.remove(fish)
                    Wugui.eat()
                    print(f"乌龟吃掉了一条鱼,体力增加20点")
            print(f"乌龟当前位置：({Wugui.x}, {Wugui.y})")
            print(f"乌龟体力还有{Wugui.tili}点")
            print(f"鱼还有{len(fish_lis)}条")
        if Wugui.tili <= 0:
            print("乌龟体力耗尽，游戏结束！")
        elif len(fish_lis) == 0:
            print("所有鱼被吃掉，乌龟胜利！")
view = View()
view.main()

# 3.定义一个学生类
# 1.有下面的类属性：姓名 年龄 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 2.类方法
# 1） 获取学生的姓名：get_name() 返回类型:str
# 2 ）获取学生的年龄：get_age() 返回类型:int
# 3 ）返回3门科目中最高的分数：get_course() 返回类型:int
# class Student(object):
#     def __init__(self, name, age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_course(self,):
#         max_score = max(self.score)
#         return max_score
# student = Student("RZZ",18,[80,60,30])
# print(student.get_name())
# print(student.get_age())
# print(student.get_course())

#
# 4.封装百分制分数 （函数）
# 封装百分制分数，和它对应的五档分制分数
# def scores(score):
#     if score >= 90:
#         grade = "优秀"
#     elif score >= 80:
#         grade = "良好"
#     elif score >= 70:
#         grade = "中等"
#     elif score >= 60:
#         grade = "及格"
#     else:
#         grade = "gun"
#
#     return grade
# score = int(input("请输入你的分数："))
# scores(score)
# print(f"百分制分数 {score} 对应的五档分制分数是 {scores(score)}")


#
# 5.工资结算系统。
# 要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，
# 根据提供的员工信息来计算员工的月薪。其中，部门经理的月薪是固定15000元；程序员按工作时间（
# 以小时为单位）支付月薪，每小时200元；销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。
# class Salary(object):
#     def __init__(self):
#         self.salary= None
#     def manager(self):
#         print("部门经理该月工资为：15000元")
#     def programmer(self,time):
#         self.salary = 200*time
#         print(f"程序员该月工资为{self.salary}元")
#     def salesman(self,sale):
#         self.salary = 1800 + sale
#         print(f"销售员该月工资为{self.salary}元")
# class View(object):
#     def menu(self):
#         print('*'*50)
#         print("工资系统：\n"
#               "\t\t1.部门经理\n"
#               "\t\t2.程序员\n"
#               "\t\t3.销售员")
#         print('*' * 50)
#     def display(self):
#         salary1 = Salary()
#         self.menu()
#         while True:
#             choice = input("请输入要查询的职位：")
#             if choice == '1':
#                 salary1.manager()
#             elif choice == '2':
#                 time = int(input("请输入工作的时间："))
#                 salary1.programmer(time)
#             elif choice == '3':
#                 sala = int(input("请输入该月销售额:"))
#                 salary1.salesman(sala)
#             else:
#                 print("选择错误")
# view = View()
# view.display()














