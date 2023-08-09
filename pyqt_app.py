from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
from random import randint


class Ui_MainWindow(object):
    def __init__(self):
        self.label_day = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 60, 650, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, "
            "0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, "
            "64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, "
            "128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.title_label.setObjectName("title_label")
        self.oleg_pic = QtWidgets.QLabel(self.centralwidget)
        self.oleg_pic.setGeometry(QtCore.QRect(700, 0, 141, 211))
        self.oleg_pic.setObjectName("oleg_pic")
        self.label_day = QtWidgets.QLabel(self.centralwidget)
        self.label_day.setGeometry(QtCore.QRect(110, 320, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_day.setFont(font)
        self.label_day.setStyleSheet("border-style: ridge;\n"
                                     "border-color: rgb(255, 0, 0);\n"
                                     "border-width: 6px;")
        self.label_day.setObjectName("label_day")
        self.label_month = QtWidgets.QLabel(self.centralwidget)
        self.label_month.setGeometry(QtCore.QRect(290, 320, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_month.setFont(font)
        self.label_month.setStyleSheet("border-style: ridge;\n"
                                       "border-color: rgb(0, 255, 0);\n"
                                       "border-width: 6px;")
        self.label_month.setObjectName("label_month")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(480, 320, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_year.setFont(font)
        self.label_year.setStyleSheet("border-style: ridge;\n"
                                      "border-color: rgb(0, 0, 255);\n"
                                      "border-width: 6px;")
        self.label_year.setObjectName("label_year")

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(720, 320, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("border-style: ridge;\n"
                                        "border-color: rgb(211, 220, 50);\n"
                                        "border-width: 6px;")
        self.label_result.setObjectName("label_result")
        self.label_result.setWordWrap(True)
        self.guessbtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.guessbtn_1.setGeometry(QtCore.QRect(100, 410, 101, 61))
        self.guessbtn_1.setStyleSheet("font: 16pt \"Swis721 BdOul BT\";\n"
                                      "color: rgb(265, 190, 255);\n"
                                      "background-color: rgb(170, 170, 255);")
        self.guessbtn_1.setObjectName("guessbtn_1")
        self.guessbtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.guessbtn_2.setGeometry(QtCore.QRect(280, 410, 101, 61))
        self.guessbtn_2.setStyleSheet("font: 16pt \"Swis721 BdOul BT\";\n"
                                      "color: rgb(265, 190, 255);\n"
                                      "background-color: rgb(170, 170, 255);")
        self.guessbtn_2.setObjectName("guessbtn_2")
        self.guessbtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.guessbtn_3.setGeometry(QtCore.QRect(470, 410, 101, 61))
        self.guessbtn_3.setStyleSheet("font: 16pt \"Swis721 BdOul BT\";\n"
                                      "color: rgb(265, 190, 255);\n"
                                      "background-color: rgb(170, 170, 255);")
        self.guessbtn_3.setObjectName("guessbtn_3")
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setGeometry(QtCore.QRect(750, 410, 101, 61))
        self.find_btn.setStyleSheet("font: 16pt \"Swis721 BdOul BT\";\n"
                                    "color: rgb(265, 190, 255);\n"
                                    "background-color: rgb(170, 170, 255);")
        self.find_btn.setObjectName("find_btn")
        self.conclusion_label = QtWidgets.QLabel(self.centralwidget, wordWrap=True)
        self.conclusion_label.setGeometry(QtCore.QRect(200, 530, 571, 351))
        self.conclusion_label.setText("")
        self.conclusion_label.setObjectName("conclusion_label")
        font.setPointSize(14)
        self.conclusion_label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "казино"))
        self.title_label.setText(_translate("MainWindow", "Когда Олег Юрьевна станет адекватом?"))
        self.oleg_pic.setText(
            _translate("MainWindow", '<html><head/><body><p><img src="orlova.png"/></p></body></html>'))
        self.label_day.setText(_translate("MainWindow", "Число"))
        self.label_month.setText(_translate("MainWindow", "Месяц"))
        self.label_year.setText(_translate("MainWindow", "Год"))
        self.label_result.setText(_translate("MainWindow", "Результат:"))
        self.guessbtn_1.setText(_translate("MainWindow", "Guess"))
        self.guessbtn_2.setText(_translate("MainWindow", "Guess"))
        self.guessbtn_3.setText(_translate("MainWindow", "Guess"))
        self.find_btn.setText(_translate("MainWindow", "find out"))

    def add_functions(self, MainWindow):
        print(0)
        self.timer_seconds = 0
        self.guessbtn_1.clicked.connect(lambda: self.main_guess(1))
        self.guessbtn_2.clicked.connect(lambda: self.main_guess(2))
        self.guessbtn_3.clicked.connect(lambda: self.main_guess(3))
        self.find_btn.clicked.connect(lambda: self.main_guess(4))
        print(-1)

    def main_guess(self, choice):
        if self.timer_seconds == 0:
            self.timer = QtCore.QTimer()
            if choice == 4:
                self.timer.setInterval(300)
            else:
                self.timer.setInterval(100)
            self.timer.timeout.connect(lambda: self.generate_string(choice))
            print(2)
            self.timer.start()
            print(3)
        else:
            pass

    def generate_string(self, choice):
        if choice == 1:
            self.label_day.setText(str(randint(1, 32)))
            self.timer_seconds += 1
        elif choice == 2:
            arr = ['Декабря', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября',
                   'Ноября', 'Января']
            self.label_month.setText(arr[randint(0, 11)])
            self.timer_seconds += 1
        elif choice == 3:
            self.label_year.setText(str(randint(2030, 2100)))
            self.timer_seconds += 1
        elif choice == 4 and self.label_month.text() != "Месяц" and self.label_day.text() != "Число" and self.label_year.text() != "Год":
            if self.timer_seconds == 0:
                self.label_result.setText('Результат негативный')
                self.label_result.adjustSize()
            arr = ['Ты серьезно', ' думал что оно', ' может стать нормальным', ' о_О? какой наивный',
                   ' жееесть... Расскажу п0', ' секрету - она ест учен', 'иков после плохо', 'й сдачи егэ поэтому',
                   ' она себя квалифицирует', ' как топ учителя у ', 'которого онли стобаль', 'ники. в общем гуляйй']
            self.conclusion_label.setText(f'{self.conclusion_label.text()}{arr[self.timer_seconds]}')
            self.timer_seconds += 1
            #self.conclusion_label.adjustSize()
        if self.timer_seconds == 12 and choice == 4:
            self.timer.stop()
            self.timer_seconds = 0
        elif self.timer_seconds == 20:
            self.timer.stop()
            self.timer_seconds = 0

    def guess1(self, MainWindow):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.onTimeout)
        timer.start(2000)
        print(1)
        self.label_day.setText(str(randint(1, 32)))
        for i in range(20):
            self.label_day.setText(str(randint(1, 32)))
            MainWindow.show()
            time.sleep(0.5)
            print(1)

    def guess2(self):
        print(1)

    def guess3(self):
        pass

    def show_result(self):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


