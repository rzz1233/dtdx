# 士兵突击
# 需求
# 1. 士兵 许三多 有一把 AK47
# 2. 士兵 可以 开火
# 3. 枪 能够 发射 子弹
# 4. 枪 装填 装填子弹 —— 增加子弹数量


class Gun:
    def __init__(self,gun_type):
        self.gun_type = gun_type
        self.free_bullet = 1
    def shoots(self):
        if self.free_bullet <= 0:
            print("没有子弹了...")
        else:
            self.free_bullet -= 1
            print(f"发射成功")

    def add_bullet(self,num2):
        self.free_bullet += num2
        if self.free_bullet < 30:
            print(f"装填了{num2}颗子弹")
        else:
            print("超出子弹装填范围，现枪中子弹为30")
            self.free_bullet = 30
gun = Gun('AK47')

# gun.shoots()
# gun.shoots()
# gun.shoots()
# gun.add_bullet(2)
# gun.shoots()

class Soldier:
    def __init__(self,name):
        self.gun = Gun('ak47')
        self.name = name
        self.gun_name = 'ak47'
    def fire(self):
        if self.gun_name is None:
            print("没有枪")
        self.gun.shoots()
        self.gun.add_bullet(10)

soldier = Soldier("许三多")
soldier.fire()







