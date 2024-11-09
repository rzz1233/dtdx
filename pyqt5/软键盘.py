import sys
# 界面
from PyQt5.QtWidgets import QWidget,QApplication
from functools import partial
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
        self.setGeometry(200, 100, 1200, 600)
        self.setWindowTitle('软键盘')
        # 背景图
        img = QPixmap('风景.jpg')
        img = img.scaled(self.size(), Qt.KeepAspectRatio)
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(img)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.setScaledContents(True)
        # 栅格化
        self.grid = QGridLayout()

        # 单行文本编辑器
        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(1000,100)
        self.line_edit.setReadOnly(True) #设置为只读
        self.line_edit.setStyleSheet("font-size: 30px;font-family: 宋体;")

        # 按钮
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('4', 1, 3),('5', 1, 4), ('6', 1, 5), ('7', 1, 6), ('8', 1, 7), ('9', 1, 8), ('0', 1, 9),
            ('=', 2, 0), ('Q', 2, 1), ('W', 2, 2), ('E', 2, 3),('R', 2, 4), ('T', 2, 5), ('Y', 2, 6), ('U', 2, 7), ('I', 2, 8), ('O', 2, 9),
            ('P', 3, 0), ('A', 3, 1), ('S', 3, 2), ('D', 3, 3),('F', 3, 4), ('G', 3, 5), ('H', 3, 6), ('J', 3, 7), ('K', 3, 8), ('L', 3, 9),
            ('Z',4 , 0), ('X',4 , 1), ('C',4 , 2), ('V',4 , 3),('B',4 , 4), ('N',4 , 5), ('M',4 , 6), (',',4 , 7), ('.',4 , 8), ('?', 4, 9),
            ("BACK",1,10), ("|",2,10),("return",3,10),("Shift",4,10),("Ctrl",5,0)
        ]
        for text, row, col in buttons:
            self.button = QPushButton(text)
            self.button.setFixedSize(70,70)
            # self.button.setStyleSheet("background-color: black;color:white;font-size: 20px;")
            self.button.setStyleSheet("font-size: 20px;")
            self.grid.addWidget(self.button, row, col)
            if text == 'BACK':
                self.button.clicked.connect(self.backspace)

            else:
            #点击按钮将其写入文本框
                self.button.clicked.connect(partial(self.addToExpression, text))
        self.button1 = QPushButton('space')
        self.button1.setStyleSheet("font-size: 20px;")
        self.button1.setFixedSize(430, 70)
        self.grid.addWidget(self.button1, 5,1,1,5)
        self.button1.clicked.connect(partial(self.addToExpression,"space"))

        # 将控件添加栅格化布局中
        self.grid.addWidget(self.line_edit, 0, 0, 1, 11)
        # 设置整体布局（布局方式）只能有一个
        self.setLayout(self.grid)

        # 键盘事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Backspace:
            self.backspace()
        elif event.key() == Qt.Key_W:
            self.addToExpression("w")

    # 加入文本框中
    def addToExpression(self, char):
        current_text = self.line_edit.text()
        if char == 'space':
            new_text = current_text + " "
            self.line_edit.setText(new_text)
        else:
            # current_text = self.line_edit.text()
            new_text = current_text + char
            self.line_edit.setText(new_text)
    # 退格
    def backspace(self):
        current_text = self.line_edit.text()
        new_text = current_text[:len(current_text) - 1]
        self.line_edit.setText(new_text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())