# 实现对学生信息的增加、删除、修改和查询。
class Student:
    def __init__(self):
        self.__id = None
        self.__name=None
        self.__age=None
        self.__score=None
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score
class Stu_manage:
    def __init__(self):
        self.__lis = []
    @property
    def lis(self):
        return self.__lis
    def add_student(self,stu):
        self.__lis.append(stu)
    def del_stu(self,id):
        for stu in self.__lis:
            if stu.id == id:
                self.__lis.remove(stu)
    def update(self,stu):
        for i in self.__lis:
            if i.id == stu.id:
                i.name = stu.name
                i.age = stu.age
                i.score = stu.score
    def sort(self):
        new_lis= self.__lis.copy()
        for i in range(len(new_lis)-1):
            for j in range(i+1,len(new_lis)):
                if int(new_lis[i].score) < int(new_lis[j].score):
                    new_lis[i],new_lis[j] = new_lis[j],new_lis[i]

        for a in new_lis:
            print(a.name)

class Stu_view:
    def __init__(self):
        self.__stu_manage = Stu_manage()#当对象是私有的时候需要将其进行实例化(self.__stu_manage就是对象)
    def add_students(self):
        stu = Student()
        stu.id = input("请输入学生学号：")
        stu.name = input("请输入学生名字：")
        stu.age = input("请输入学生年龄：")
        stu.score = input("请输入学生成绩：")
        self.__stu_manage.add_student(stu)
    def upadtes(self):
        stu = Student()
        stu.id = input("请输入要修改的学生学号：")
        stu.name = input("请输入要修改的学生名字：")
        stu.age = input("请输入要修改的学生年龄：")
        stu.score = input("请输入要修改的学生成绩：")
        self.__stu_manage.update(stu)
    def del_stus(self):
        id = input("请输入要删除的学号：")
        self.__stu_manage.del_stu(id)

    def print(self,lis):
        if len(lis) == 0:
            print("没有学生信息")
        else:
            for i in lis:
                print(f"学号:{i.id} 姓名:{i.name} 年龄:{i.age} 成绩:{i.score}")
    def __menu(self):
        print("*"*50)
        print('欢迎来到信息管理系统\n'
              '你可以进行如下操作:')
        print("\t\t1. 添加学生信息")
        print("\t\t2. 修改学生信息")
        print("\t\t3. 删除学生信息")
        print("\t\t4. 查看学生信息")
        print("\t\t5. 排序")
        print("\t\tq. 退出")
        print("*"*50)
    def __select(self):
        while True:
            choice = input("请输入你的选择：")
            if choice == '1':
                self.add_students()
            elif choice == '2':
                self.upadtes()
            elif choice == '3':
                self.del_stus()
            elif choice == '4':
                self.print(self.__stu_manage.lis)
            elif choice == '5':
                self.__stu_manage.sort()
            elif choice == 'q':
                print("已退出")
                break
            else:
                print("没有此操作")
#如果是私有方法要调用，可以将它放在一个内部方法中然后调用这个内部方法
    def main(self):
        self.__menu()
        self.__select()

stu_view = Stu_view()
stu_view.main()


















