import sys
# 界面
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
# 控件
from PyQt5.QtWidgets import QLineEdit,QPushButton,QLabel,QFrame,QMessageBox
# 布局
from PyQt5.QtWidgets import QVBoxLayout,QGridLayout # 水平 垂直  栅格化

import logging
logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    filemode='a',
                    encoding='utf-8',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.cartList = []
        self.goodList = [{'name': '笔记本电脑', 'price': 8000}, {'name': '鼠标', 'price': 100}]
        self.collectSet = set()
        self.createwindow()
    def createwindow(self):
        self.setGeometry(500,200,500,500)
        self.setWindowTitle('购物车')

        img = QPixmap('购物车背景图.jpg')
        img = img.scaled(self.size(), Qt.KeepAspectRatio)
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(img)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.setScaledContents(True)

        self.vbox = QVBoxLayout()
        self.lab = QLabel("欢迎来到购物车，有以下操作：")
        self.lab.setFixedSize(300, 60)
        self.lab.setStyleSheet("color:black;font-size: 20px;font-family: 宋体;")
        self.button1 = QPushButton("1. 加入购物车")
        self.button2 = QPushButton("2. 收藏商品")
        self.button3 = QPushButton("3. 删除购物车商品")
        self.button4 = QPushButton("4. 去结算")
        self.button5 = QPushButton("5. 清空购物车")
        self.button6 = QPushButton("6. 查看购物车")
        self.button7 = QPushButton("7. 添加新商品")
        self.button8 = QPushButton("8. 查看商品")
        self.button9 = QPushButton(" 退出")
        self.vbox.addWidget(self.lab)
        self.vbox.addWidget(self.button1)
        self.vbox.addWidget(self.button2)
        self.vbox.addWidget(self.button3)
        self.vbox.addWidget(self.button4)
        self.vbox.addWidget(self.button5)
        self.vbox.addWidget(self.button6)
        self.vbox.addWidget(self.button7)
        self.vbox.addWidget(self.button8)
        self.vbox.addWidget(self.button9)
    #绑定事件

        self.button1.clicked.connect(self.open_addcart)
        self.button2.clicked.connect(self.open_collectSet)
        self.button3.clicked.connect(self.open_delcart)
        self.button4.clicked.connect(self.open_buy)
        self.button5.clicked.connect(self.clear_cart)
        self.button6.clicked.connect(self.check_cart)
        self.button7.clicked.connect(self.open_addgoods)
        self.button8.clicked.connect(self.open_goods)
        self.button9.clicked.connect(self.quit)



        self.setLayout(self.vbox)
    #打开加入购物车窗口
    def open_addcart(self):
        self.addcartwindow= addcartWindow(self.cartList,self.goodList)
        self.addcartwindow.show()

    #打开加入收藏窗口
    def open_collectSet(self):
        self.collwindow = collWindow(self.collectSet,self.goodList)
        self.collwindow.show()

    #删除购物车商品
    def open_delcart(self):
        self.del_window = delWindow(self.cartList)
        self.del_window.show()

    #结算购物车商品
    def open_buy(self):
        self.buy_cart = Buy_cart(self.cartList)
        self.buy_cart.show()

    #清空购物车
    def clear_cart(self):
        self.cartList.clear()
        QMessageBox.information(self,"清空购物车","已清空购物车",QMessageBox.Ok)

    #打开查看购物车窗口
    def check_cart(self):
        self.check_cart = Check_cart(self.cartList)
        self.check_cart.show()

    #打开添加新商品窗口
    def open_addgoods(self):
        self.add_goods_window = Add_goods_Window(self.goodList)
        self.add_goods_window.show()

    #打开商品窗口
    def open_goods(self):
        self.goods_window = goodsWindow(self.goodList)
        self.goods_window.show()
    #退出
    def quit(self):
        self.close()

#加入购物车窗口
class addcartWindow(QWidget):
    def __init__(self,cartlist,goodList):
        super().__init__()
        self.cartList = cartlist
        self.goodList = goodList
        self.initUI()
    def initUI(self):
        # self.setGeometry(500, 200, 500, 400)
        self.setWindowTitle('加入购物车')
        self.vbox = QVBoxLayout()

        self.lab1 = QLabel("请输入要加入的商品：")
        self.line1 = QLineEdit()
        self.lab2 = QLabel("请输入要加入的商品数量：")
        self.line2 = QLineEdit()
        self.button = QPushButton("添加")

        self.vbox.addWidget(self.lab1)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.lab2)
        self.vbox.addWidget(self.line2)
        self.vbox.addWidget(self.button)

        self.button.clicked.connect(self.add_cart)

        self.setLayout(self.vbox)
    def add_cart(self):

        name = self.line1.text()
        number = self.line2.text()
        goods = {}
        for good in self.goodList:
            if name == good['name']:
                if number == "":
                    goods['name'] = good['name']
                    goods['price'] = good['price']
                    goods['number'] = 1
                else:
                    goods['name'] = good['name']
                    goods['price'] = good['price']
                    goods['number'] = int(number)
        if goods != {}:
            if self.cartList == []:
                self.cartList.append(goods)
                QMessageBox.information(self,"添加成功","该商品添加成功",QMessageBox.Ok)
                self.close()
            else:
                for cart in self.cartList:
                    if cart['name'] == goods['name']:
                        cart['number'] = cart['number'] + int(number)
                        QMessageBox.information(self, "添加成功", "该商品添加成功", QMessageBox.Ok)
                        self.close()
                        break
                else:
                    self.cartList.append(goods)
                    QMessageBox.information(self,"添加成功","该商品添加成功",QMessageBox.Ok)
                    self.close()
        else:
            QMessageBox.warning(self,"添加失败","没有该商品",QMessageBox.Ok)
#收藏
class collWindow(QWidget):
    def __init__(self,collect,goodlist):
        super().__init__()
        self.collect = collect
        self.goodlist = goodlist
        self.initUI()
    def initUI(self):
        self.setWindowTitle('收藏')
        self.vbox = QVBoxLayout()
        self.lab1 = QLabel("加入收藏的商品")
        self.line1 = QLineEdit()
        self.button = QPushButton("添加")
        self.button1 = QPushButton("查看收藏列表")
        self.vbox.addWidget(self.lab1)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.button1)

        self.button.clicked.connect(self.add_coll)
        self.button1.clicked.connect(self.open_look_coll)
        self.setLayout(self.vbox)
    def add_coll(self):
        name = self.line1.text()
        if name == "":
            QMessageBox.warning(self, "添加失败", "添加的商品为空", QMessageBox.Ok)

        else:
            for good in self.goodlist:
                if name == good['name']:
                    self.collect.add(name)
                    QMessageBox.information(self, "添加成功", "该商品已添加到收藏列表", QMessageBox.Ok)
                    break
            else:
                QMessageBox.warning(self, "添加失败", "不在商品列表里", QMessageBox.Ok)

    def open_look_coll(self):
        self.look_coll = Look_coll(self.collect)
        self.look_coll.show()


# 删除购物车商品
class delWindow(QWidget):
    def __init__(self,cartlist):
        super().__init__()
        self.cartlist = cartlist
        self.initUI()
    def initUI(self):
        self.setWindowTitle('删除购物车商品')
        self.grid = QGridLayout()
        self.lab1 = QLabel("要删除的商品：")
        self.line1 = QLineEdit()
        self.button = QPushButton("删除")
        self.grid.addWidget(self.lab1,0,0,1,1)
        self.grid.addWidget(self.line1,0,1,1,2)
        self.grid.addWidget(self.button,1,0,1,3)

        self.button.clicked.connect(self.del_cart)
        self.setLayout(self.grid)
    def del_cart(self):
        name = self.line1.text()
        if len(self.cartlist) == 0:
            QMessageBox.warning(self,"删除失败","要删除的商品为空", QMessageBox.Ok)
        else:
            for cart in self.cartlist:
                if cart['name'] == name:
                    self.cartlist.remove(cart)
                    QMessageBox.information(self, "删除成功", f"{name}已被删除", QMessageBox.Ok)
                    self.close()
                    break
            else:
                QMessageBox.warning(self, "删除失败", f"购物车没有{name}", QMessageBox.Ok)

class Buy_cart(QWidget):
    def __init__(self,cartlist):
        super().__init__()
        self.cartList = cartlist
        self.initUI()
    def initUI(self):
        self.setWindowTitle('结算')
        self.vbox = QVBoxLayout()
        self.lab1 = QLabel("要结算的商品：")
        self.line1 = QLineEdit()
        self.lab2 =QLabel("结算的数量：")
        self.line2 = QLineEdit()
        self.button = QPushButton("结算")
        self.vbox.addWidget(self.lab1)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.lab2)
        self.vbox.addWidget(self.line2)
        self.vbox.addWidget(self.button)
        self.button.clicked.connect(self.jiesuan)
        self.setLayout(self.vbox)
    def jiesuan(self):
        name = self.line1.text()
        number = self.line2.text()
        sum = 0
        if len(self.cartList) == 0:
            QMessageBox.warning(self, "结算失败", "购物车为空", QMessageBox.Ok)
            logging.error('购物车为空')
        else:
            for good in self.cartList:
                if name == good['name']:
                    if number == "":
                        sum += good['price'] * good['number']
                    elif int(number) > 0 and int(number) <= int(good['number']):
                        sum += good['price'] * int(number)
                        a = good['number'] - int(number)
                        good['number'] = a
                        QMessageBox.information(self, "结算成功", f"花费{sum}", QMessageBox.Ok)
                        logging.info(f"花费{sum}")
                        self.close()

                        if good['number'] == 0:
                            self.cartList.remove(good)
                    elif int(number) > int(good['number']):
                        QMessageBox.warning(self, "结算失败", "购物车中该商品没有这么多数量", QMessageBox.Ok)
                        self.close()
                elif name == "":
                    for good in self.cartList:
                        price = good["price"]
                        number = good["number"]
                        sum += price * number
                    QMessageBox.information(self, "结算成功", f"购物车所有商品花费{sum}", QMessageBox.Ok)
                    logging.info(f"花费{sum}")
                    self.close()
                    self.cartList.clear()

#查看收藏列表
class Look_coll(QWidget):
    def __init__(self,collectList):
        super().__init__()
        self.collectList = collectList
        self.initUI()
    def initUI(self):
        self.setWindowTitle('收藏列表')
        self.vbox = QVBoxLayout()
        self.lab1 = QLabel("收藏列表：")
        self.vbox.addWidget(self.lab1)
        if len(self.collectList) == 0:
            self.lab2 = QLabel("收藏为空")
            self.vbox.addWidget(self.lab2)
        else:
            for coll in self.collectList:
                lab = QLabel(f"\t{coll}")
                self.vbox.addWidget(lab)
        self.setLayout(self.vbox)



#查看购物车
class Check_cart(QWidget):
    def __init__(self,cartList):
        super().__init__()
        self.cartList = cartList

        self.initUI()
    def initUI(self):

        self.setWindowTitle('查看购物车')
        self.vbox = QVBoxLayout()

        if len(self.cartList) == 0:
            self.lab1 = QLabel("购物车为空")
            self.vbox.addWidget(self.lab1)
        else:
            self.lab = QLabel("购物车：")
            self.vbox.addWidget(self.lab)
            for cart in self.cartList:
                name_label = QLabel(f"商品：{cart['name']} 数量： {cart['number']}价格：{cart['price']}")
                self.vbox.addWidget(name_label)
        self.setLayout(self.vbox)

#添加新商品
class Add_goods_Window(QWidget):
    def __init__(self,goodList):
        super().__init__()
        self.goodList = goodList
        self.initUI()
    def initUI(self):
        self.setWindowTitle('添加商品')
        self.vbox = QVBoxLayout()
        self.lab1 = QLabel("要添加的商品名字：")
        self.line1 = QLineEdit()
        self.lab2 = QLabel("价格：")
        self.line2 = QLineEdit()
        self.button = QPushButton("添加")
        self.vbox.addWidget(self.lab1)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.lab2)
        self.vbox.addWidget(self.line2)
        self.vbox.addWidget(self.button)
        self.button.clicked.connect(self.add_good)
        self.setLayout(self.vbox)
    def add_good(self):
        name = self.line1.text()
        price = self.line2.text()
        if len(name) == 0 or len(price) == 0:
            QMessageBox.warning(self, "添加失败", "不能为空", QMessageBox.Ok)
        elif int(price) < 0:
            QMessageBox.warning(self, "添加失败", "价格不能是负数", QMessageBox.Ok)

        else:
            goods = {}
            goods['name'] = name
            goods['price'] = int(price)
            if goods not in self.goodList:
                self.goodList.append(goods)
                QMessageBox.information(self,"添加成功","该商品已经添加到商品列表", QMessageBox.Ok)
                self.close()
            else:
                QMessageBox.warning(self, "添加失败", "已经有该商品", QMessageBox.Ok)


#商品窗口
class goodsWindow(QWidget):
    def __init__(self,goodList):
        super().__init__()
        self.goodList = goodList
        self.initUI()
    def initUI(self):
        # self.setGeometry(500, 200, 500, 400)
        self.setWindowTitle('商品列表')

        self.vbox = QVBoxLayout()
        self.lab = QLabel("商品列表：")
        self.vbox.addWidget(self.lab)
        for goods in self.goodList:
            name_label = QLabel(f"{goods['name']}: {goods['price']}")
            self.vbox.addWidget(name_label)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())