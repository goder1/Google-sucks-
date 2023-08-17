from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
import sys
import time
from random import randint

from structure_generation import Ui_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.widget_only_icons.hide()
        self.ui.pages_widget.setCurrentIndex(0)
        self.ui.analysis_1.setChecked(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

