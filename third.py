#!/usr/bin/python3
#coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Icon(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("AngelByte")
        self.setWindowIcon(QIcon('files-and-folders.png'))


        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Icon()
    sys.exit(app.exec_())
    
