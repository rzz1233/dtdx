import sys
# 界面
from PyQt5.QtWidgets import QApplication, QWidget

# 控件
from PyQt5.QtWidgets import QPushButton, QFrame
# 布局
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout

class Hide(QWidget):
    def __init__(self):
        super().__init__()
        self.hideorshow()

    def hideorshow(self):
        hbox = QHBoxLayout()

        # 创建左侧QFrame
        left = QFrame(self)
        left.setFrameShape(QFrame.StyledPanel)
        # 创建右侧QFrame
        right = QFrame(self)
        right.setFrameShape(QFrame.StyledPanel)
        right.hide()

        left_vbox = QVBoxLayout(left)
        btn = QPushButton('Hide')
        btn1 = QPushButton('Hide1')
        btn.clicked.connect(self.hideRight)
        left_vbox.addWidget(btn)
        left_vbox.addWidget(btn1)



        hbox.addWidget(left)
        hbox.addWidget(right)

        self.setLayout(hbox)

    def hideRight(self):
        widget = self.layout().itemAt(1).widget()
        print(widget.isHidden())
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Hide()
    window.show()
    sys.exit(app.exec_())