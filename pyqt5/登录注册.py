import sys, json
# 界面
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
# 控件
from PyQt5.QtWidgets import QLineEdit,QPushButton,QLabel,QFrame,QMessageBox
# 布局
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout,QGridLayout # 水平 垂直  栅格化
class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.createwindow()
        self.lis = []
    def createwindow(self):
        # self.setGeometry(500,200,500,200)
        self.setWindowTitle('登录注册')

        img = QPixmap('购物车背景图.jpg')
        img = img.scaled(self.size(), Qt.KeepAspectRatio)
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(img)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.setScaledContents(True)

        hbox = QHBoxLayout()
        # 创建左侧QFrame
        left = QFrame(self)
        left.setFrameShape(QFrame.StyledPanel)
        # 创建右侧QFrame
        right = QFrame(self)
        right.setFrameShape(QFrame.StyledPanel)
        right.hide()

     #左侧
        self.left_vbox = QVBoxLayout(left)
        # 单行文本编辑器
        self.line_edit = QLineEdit()
        self.line_pw = QLineEdit()
        #按钮
        self.button1 = QPushButton("登录")
        self.button2 = QPushButton("注册")

        self.lab1 = QLabel("账号:")
        self.lab2 = QLabel("密码：")
        self.button2.clicked.connect(self.hideRight)

        self.left_vbox.addWidget(self.lab1)
        self.left_vbox.addWidget(self.line_edit)
        self.left_vbox.addWidget(self.lab2)
        self.left_vbox.addWidget(self.line_pw)
        self.left_vbox.addWidget(self.button1)
        self.left_vbox.addWidget(self.button2)
    #右侧
        self.lab3 = QLabel("请设置用户名：")
        self.lab4 = QLabel("请设置密码：")
        self.lab5 = QLabel("请确认密码：")
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()

        self.button3 = QPushButton("注册")
        self.button3.clicked.connect(self.hideRight)


        self.right_vbox = QVBoxLayout(right)
        self.right_vbox.addWidget(self.lab3)
        self.right_vbox.addWidget(self.line3)
        self.right_vbox.addWidget(self.lab4)
        self.right_vbox.addWidget(self.line4)
        self.right_vbox.addWidget(self.lab5)
        self.right_vbox.addWidget(self.line5)
        self.right_vbox.addWidget(self.button3)

        self.button3.clicked.connect(self.register)
        self.button1.clicked.connect(self.log)
        hbox.addWidget(left)
        hbox.addWidget(right)

        # 设置整体布局（布局方式）只能有一个
        self.setLayout(hbox)
    def hideRight(self):
        widget = self.layout().itemAt(1).widget()
        # print(widget.isHidden())
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()


    def register(self):
        line3 = self.line3.text()
        line4 = self.line4.text()
        line5 = self.line5.text()


        if line4 == line5 and line3 != "" and line4 != "":
            dic1 = {}
            dic1["用户名"] = line3
            dic1["密码"] = line4

            with open("注册.txt", "w", encoding="utf-8") as f:
                self.lis.append(dic1)
                res = json.dumps(self.lis, ensure_ascii=False)
                f.write(res)
            QMessageBox.information(self,"注册成功","注册成功，欢迎",QMessageBox.Ok)
        elif line4 =="" or line3 == "":
            QMessageBox.warning(self, 'Error', '输入为空，请重新输入')

        else:
            QMessageBox.warning(self, 'Error', '密码不一致，请重新输入')
    def log(self):
        line_edit = self.line_edit.text()
        line_pw = self.line_pw.text()
        dic2={}
        dic2["用户名"] = line_edit
        dic2["密码"] = line_pw

        with open("注册.txt","r",encoding="utf-8") as f:
            res1 = f.read()
        lis = json.loads(res1)
        if dic2 not in lis:
            QMessageBox.warning(self, 'Error', '未注册请先注册', QMessageBox.Ok)
        else:
            QMessageBox.information(self, "成功", f"登录成功，欢迎{line_edit}", QMessageBox.Ok)
            self.main = Main()
            self.main.show()
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(500,200,500,400)

        self.setWindowTitle('主页面')

        img = QPixmap('购物车背景图.jpg')
        img = img.scaled(self.size(), Qt.KeepAspectRatio)
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(img)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.setScaledContents(True)

        self.vbox = QVBoxLayout()

        self.button1 = QPushButton("按钮")
        self.button2 = QPushButton("退出")
        self.button2.clicked.connect(self.quit)

        self.vbox.addWidget(self.button1)
        self.vbox.addWidget(self.button2)

        self.setLayout(self.vbox)
    def quit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())