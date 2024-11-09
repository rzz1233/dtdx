import sys
# 界面
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
# 控件
from PyQt5.QtWidgets import QLineEdit,QPushButton,QLabel
# 布局
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout,QGridLayout # 水平 垂直  栅格化
#绘制界面
class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.createwindow()
    def createwindow(self):
        self.setGeometry(300, 100, 500, 800)
        self.setWindowTitle('界面绘制')
        #背景图
        img = QPixmap('风景.jpg')
        img = img.scaled(self.size(), Qt.KeepAspectRatio)
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(img)
        self.bg_label.setGeometry(0,0,self.width(),self.height())
        self.bg_label.setScaledContents(True)
    #布局
        #水平
        self.hbox = QHBoxLayout()
        #垂直
        self.vbox = QVBoxLayout()
        #栅格化
        self.grid = QGridLayout()

        # 单行文本编辑器
        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(200, 50)
        self.line_edit.setStyleSheet("background-color: blue;color:white;font-size: 30px;"
                                     "font-family: 宋体;")
        # 按钮
        self.btn = QPushButton("登录")
        self.btn1 = QPushButton("注册")
        self.btn2 = QPushButton("注册2")
        # 将控件添加到水平布局中
        # self.hbox.addWidget(self.line_edit)
        # self.hbox.addWidget(self.btn)
        # # 将控件添加到垂直布局中
        # self.vbox.addWidget(self.line_edit)
        # self.vbox.addWidget(self.btn)
        # 将控件添加栅格化布局中
        self.grid.addWidget(self.line_edit,0,0)
        self.grid.addWidget(self.btn,0,1)
        self.grid.addWidget(self.btn1,1,0)
        self.grid.addWidget(self.btn2,1,1)

        # 绑定事件
        self.btn.clicked.connect(self.func)

        # 设置整体布局（布局方式）只能有一个
        self.setLayout(self.grid)
    #键盘事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            # print("按到了A键")
            # self.btn.click()
    def func(self):
        res = self.line_edit.text()
        # 改变控件的值
        self.line_edit.setText(res)
        print(res)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())


