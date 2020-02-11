from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import math
import random
import sys
from design3 import Ui_MainWindow

class TestUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.reverse)

    def reverse(self):
        self.ui.widget.reverse_direction()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = TestUI()
    w.show()
    sys.exit(app.exec_())