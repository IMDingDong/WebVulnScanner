# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XSS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import requests
import time
import xlsxwriter

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_XSS(object):
    def setupUi(self, XSS):
        XSS.setObjectName("XSS")
        XSS.resize(500, 601)
        self.centralwidget = QtWidgets.QWidget(XSS)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(45, 53, 21, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(45, 201, 56, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(45, 163, 401, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(196, 85, 81, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(364, 99, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(364, 63, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(45, 114, 284, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(45, 63, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(74, 55, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(45, 221, 401, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(84, 85, 81, 16))
        self.checkBox.setObjectName("checkBox")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(320, 63, 20, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(143, 56, 186, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(45, 143, 56, 12))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 17, 131, 16))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(45, 260, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(45, 320, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(45, 280, 401, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(45, 342, 401, 201))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 85)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 65)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(364, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        XSS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(XSS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        XSS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(XSS)
        self.statusbar.setObjectName("statusbar")
        XSS.setStatusBar(self.statusbar)

        self.retranslateUi(XSS)
        self.pushButton.clicked.connect(self.XssSlot_1st)
        self.pushButton_2.clicked.connect(self.XssSlot_2nd, self.checkBox_2.isChecked())
        self.checkBox.clicked.connect(self.XssCheckSlot_1st, self.checkBox.isChecked())
        self.checkBox_2.clicked.connect(self.XssCheckSlot_2nd, self.checkBox_2.isChecked())
        self.tableWidget.itemDoubleClicked['QTableWidgetItem*'].connect(self.XssTableItemSlot_1st)
        self.pushButton_3.clicked.connect(self.XssSlot_3rd)
        QtCore.QMetaObject.connectSlotsByName(XSS)
        XSS.setTabOrder(self.checkBox, self.checkBox_2)
        XSS.setTabOrder(self.checkBox_2, self.lineEdit)
        XSS.setTabOrder(self.lineEdit, self.lineEdit_2)
        XSS.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        XSS.setTabOrder(self.lineEdit_3, self.pushButton)
        XSS.setTabOrder(self.pushButton, self.pushButton_2)
        XSS.setTabOrder(self.pushButton_2, self.tableWidget)

        self.pushButton_3.setVisible(False)

    def XssSlot_1st(self):
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.tableWidget.setRowCount(0)
        self.pushButton_3.setVisible(False)

    def XssSlot_2nd(self, Check2):
        if Check2:
            method = "post"
        else:
            method = "get"

        url = self.lineEdit.text()
        parameters = self.lineEdit_2.text().replace(" ", "").split(',')
        cookies_list = self.lineEdit_3.text().replace(" ", "").replace(";", "=").split("=")

        if not cookies_list[0] == '':
            cookies = {cookies_list[i]: cookies_list[i + 1] for i in range(0, len(cookies_list), 2)}

        row_number = 0

        if parameters[0] == '':
            f = open('XssPayloads.txt', 'r')

            for j in f.read().splitlines():
                XSSPayload = url + '{0}'.format(j)
                print(XSSPayload)
                if method == "get":
                    if cookies_list[0] == '':
                        response = requests.get(XSSPayload)
                    else:
                        response = requests.get(XSSPayload, cookies=cookies)
                elif method == "post":
                    if cookies_list[0] == '':
                        response = requests.post(XSSPayload)
                    else:
                        response = requests.post(XSSPayload, cookies=cookies)
                XSSCheckList = "XSS"
                if '{0}'.format(j) in response.text:
                    XSSResult = "취약"
                    time.sleep(1)

                    self.tableWidget.insertRow(row_number)
                    self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(XSSCheckList))
                    self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(XSSPayload))
                    self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(XSSResult))
                    row_number += 1
                else:
                    XSSResult = "안전"

                    self.tableWidget.insertRow(row_number)
                    self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(XSSCheckList))
                    self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(XSSPayload))
                    self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(XSSResult))
                    row_number += 1
        else:
            for parameter in parameters:
                f = open('XssPayloads.txt', 'r')
                for j in f.read().splitlines():
                    XSSPayload = url + '?' + parameter + '=' + '{0}'.format(j)
                    print(XSSPayload)
                    if method == "get":
                        if cookies_list[0] == '':
                            response = requests.get(XSSPayload)
                        else:
                            response = requests.get(XSSPayload, cookies=cookies)
                    elif method == "post":
                        if cookies_list[0] == '':
                            response = requests.post(XSSPayload)
                        else:
                            response = requests.post(XSSPayload, cookies=cookies)
                    XSSCheckList = "XSS"
                    if '{0}'.format(j) in response.text:
                        XSSResult = "취약"
                        time.sleep(1)

                        self.tableWidget.insertRow(row_number)
                        self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(XSSCheckList))
                        self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(XSSPayload))
                        self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(XSSResult))
                        row_number += 1
                    else:
                        XSSResult = "안전"

                        self.tableWidget.insertRow(row_number)
                        self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(XSSCheckList))
                        self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(XSSPayload))
                        self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(XSSResult))
                        row_number += 1

        self.pushButton_3.setVisible(True)

    def XssCheckSlot_1st(self, Check):
        if Check:
            self.checkBox.setChecked(True)
            self.checkBox_2.setChecked(False)
        else:
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(True)

    def XssCheckSlot_2nd(self, Check2):
        if Check2:
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox.setChecked(True)
            self.checkBox_2.setChecked(False)

    def XssTableItemSlot_1st(self, clickedIndex):
        row = clickedIndex.row()
        item1 = self.tableWidget.item(row, 0)
        item2 = self.tableWidget.item(row, 1)
        item3 = self.tableWidget.item(row, 2)

        QMessageBox.about(None, "XSS 점검결과 " + str(row + 1) + "번",
                          "점검항목 : " + item1.text() + "\n페이로드 : " + item2.text() + "\n점검결과 : " + item3.text())

    def XssSlot_3rd(self):

        workbook = xlsxwriter.Workbook("XSS_WebVulnScan_report.xlsx")
        worksheet = workbook.add_worksheet()

        Rows = self.tableWidget.rowCount()

        center = workbook.add_format({'align': 'center'})

        expenses = (
            ['번호', '점검항목', '페이로드', '점검결과'],
        )

        row = 1
        col = 1

        for item1, item2, item3, item4 in (expenses):
            worksheet.write(row, col, item1, center)
            worksheet.write(row, col + 1, item2, center)
            worksheet.write(row, col + 2, item3, center)
            worksheet.write(row, col + 3, item4, center)
            row += 1

        for Num in range(0, Rows):
            worksheet.write(row, col, Num + 1, center)
            worksheet.write(row, col + 1, self.tableWidget.item(Num, 0).text())
            worksheet.write(row, col + 2, self.tableWidget.item(Num, 1).text())
            worksheet.write(row, col + 3, self.tableWidget.item(Num, 2).text())
            row += 1

        worksheet.set_default_row(20)

        worksheet.set_column(1, 1, 10)
        worksheet.set_column(2, 2, 30)
        worksheet.set_column(3, 3, 80)
        worksheet.set_column(4, 4, 20)

        workbook.close()

    def retranslateUi(self, XSS):
        _translate = QtCore.QCoreApplication.translate
        XSS.setWindowTitle(_translate("XSS", "XSS"))
        self.label_4.setText(_translate("XSS", "매개변수"))
        self.lineEdit.setToolTip(_translate("XSS",
                                            "<html><head/><body><p>점검할 URL 주소를 입력해주세요.</p><p>ex) http://testWeb.kr/testXSS.jsp/</p></body></html>"))
        self.lineEdit.setWhatsThis(_translate("XSS", "<html><head/><body><p><br/></p></body></html>"))
        self.checkBox_2.setText(_translate("XSS", "POST"))
        self.pushButton_2.setText(_translate("XSS", "실행"))
        self.pushButton.setText(_translate("XSS", "초기화"))
        self.label_2.setText(_translate("XSS", "메소드 방식"))
        self.lineEdit_2.setToolTip(_translate("XSS",
                                              "<html><head/><body><p>점검할 입력필드를 입력해주세요. 여러개라면 나열해서 입력해주시면 됩니다.</p><p>ex) name, value</p></body></html>"))
        self.checkBox.setText(_translate("XSS", "GET"))
        self.label_3.setText(_translate("XSS", "URL"))
        self.label.setText(_translate("XSS", "XSS"))
        self.label_5.setText(_translate("XSS", "Cookie"))
        self.label_6.setText(_translate("XSS", "점검 결과"))
        self.lineEdit_3.setToolTip(_translate("XSS",
                                              "<html><head/><body><p>쿠키가 필요하다면 쿠키 값을 입력해주세요.</p><p>ex) cookie1=test1; cookie2=test2</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("XSS", "점검항목"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("XSS", "페이로드"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("XSS", "점검결과"))
        self.pushButton_3.setText(_translate("XSS", "보고서"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    XSS = QtWidgets.QMainWindow()
    ui = Ui_XSS()
    ui.setupUi(XSS)
    XSS.show()
    sys.exit(app.exec_())

