import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit Example')
        self.setGeometry(300, 100, 700, 800)

        # 创建 QTextEdit 组件
        self.text_edit = QTextEdit()
        self.text_edit.setFixedSize(500,600)


        # 设置初始文本内容
        # self.text_edit.setPlainText('Welcome to QTextEdit!')

        # 添加 QTextEdit 到布局
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        # 创建一个主 Widget，并设置布局
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # 设置主 Widget 为中心 Widget
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())