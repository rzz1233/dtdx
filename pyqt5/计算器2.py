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
        self.setGeometry(500, 300, 500, 600)
        self.setWindowTitle('计算器')
        # 栅格化
        self.grid = QGridLayout()

        # 单行文本编辑器
        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(500,100)
        self.line_edit.setReadOnly(True) #设置为只读
        self.line_edit.setStyleSheet("font-size: 30px;font-family: 宋体;")

        # 按钮
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ("C", 5, 0), ('CE', 5, 1), ('backspace', 5, 2), ('%', 5, 3)

        ]
        for text, row, col in buttons:
            self.button = QPushButton(text)
            self.button.setFixedSize(100,70)
            self.button.setStyleSheet("background-color: black;color:white;font-size: 20px;")
            self.grid.addWidget(self.button, row, col)
            if text == '=':
                self.button.clicked.connect(self.calculateResult)
            elif text == 'C' or text == 'CE':
                self.button.clicked.connect(self.clearEntry)
            elif text == 'backspace':
                self.button.clicked.connect(self.backspace)
            else:
            #点击按钮将其写入文本框
                self.button.clicked.connect(partial(self.addToExpression, text))

        # 将控件添加栅格化布局中
        self.grid.addWidget(self.line_edit, 0, 0, 1, 4)
        # 设置整体布局（布局方式）只能有一个
        self.setLayout(self.grid)

    #清空文本框
    def clearEntry(self):
        self.line_edit.clear()
    # 加入文本框中
    def addToExpression(self, char):
        current_text = self.line_edit.text()
        new_text = current_text + char
        self.line_edit.setText(new_text)
    # 退格
    def backspace(self):
        current_text = self.line_edit.text()
        new_text = current_text[:len(current_text) - 1]
        self.line_edit.setText(new_text)
    #计算
    def calculateResult(self):
        try:
            expression = self.line_edit.text()
            result = eval(expression)
            self.line_edit.setText(str(result))
        except Exception as e:
            self.line_edit.setText('错误')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())

