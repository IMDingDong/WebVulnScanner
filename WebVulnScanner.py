# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebVulnScanner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from XSS import Ui_XSS
from SQLi import Ui_SQLi
from LFI import Ui_LFI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 270, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("함초롬바탕")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 340, 101, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.MainSlot_1st)
        self.pushButton_2.clicked.connect(self.MainSlot_2nd)
        self.pushButton_3.clicked.connect(self.MainSlot_3rd)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def MainSlot_1st(self):
        self.XSS = QtWidgets.QMainWindow()
        self.ui = Ui_XSS()
        self.ui.setupUi(self.XSS)
        self.XSS.show()

    def MainSlot_2nd(self):
        self.SQLi = QtWidgets.QMainWindow()
        self.ui = Ui_SQLi()
        self.ui.setupUi(self.SQLi)
        self.SQLi.show()

    def MainSlot_3rd(self):
        self.LFI = QtWidgets.QMainWindow()
        self.ui = Ui_LFI()
        self.ui.setupUi(self.LFI)
        self.LFI.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "웹 취약점 스캐너"))
        self.pushButton.setText(_translate("MainWindow", "XSS"))
        self.pushButton_2.setText(_translate("MainWindow", "SQL 인젝션"))
        self.label.setText(_translate("MainWindow", "웹 취약점 스캐너"))
        self.pushButton_3.setText(_translate("MainWindow", "LFI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

