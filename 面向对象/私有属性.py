class Women:
    def __init__(self, name):
        self.name = name
        # 不要问女生的年龄
        self.__age = 18
    def __secret(self):
        print("我的年龄是 %d" % self.__age)
xiaofang = Women("小芳") # 私有属性，外部不能直接访问
print(xiaofang.__age) # 私有方法，外部不能直接调用
xiaofang.__secret()