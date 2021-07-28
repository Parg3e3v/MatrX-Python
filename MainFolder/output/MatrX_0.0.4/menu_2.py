# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tst2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.label_2.setToolTipDuration(-1)
        self.label_2.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 103, 118, 255), stop:1 rgba(0, 0, 0, 255))")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 100, 120, 15))
        self.label.setStyleSheet("font-family: Impact, Charcoal, sans-serif;\n"
"letter-spacing: 2px;\n"
"word-spacing: 2px;\n"
"color: #000000;\n"
"font-weight: 400;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: normal;\n"
"text-transform: none;\n"
"color: rgb(0, 173, 188)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.myButton = QtWidgets.QPushButton(Dialog)
        self.myButton.setEnabled(True)
        self.myButton.setGeometry(QtCore.QRect(265, 270, 110, 50))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.myButton.setFont(font)
        self.myButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.545, y2:1, stop:0 rgba(44, 104, 99, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    color: rgb(62, 255, 243);\n"
"    border: none;\n"
"    font-family: Impact, Charcoal, sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.511, y2:1, stop:0 rgba(72, 170, 162, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.myButton.setCheckable(False)
        self.myButton.setDefault(False)
        self.myButton.setFlat(False)
        self.myButton.setObjectName("myButton")
        self.MatrX_text = QtWidgets.QLabel(Dialog)
        self.MatrX_text.setGeometry(QtCore.QRect(0, 0, 640, 130))
        self.MatrX_text.setMinimumSize(QtCore.QSize(0, 0))
        self.MatrX_text.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.MatrX_text.setFont(font)
        self.MatrX_text.setMouseTracking(False)
        self.MatrX_text.setStyleSheet("font-family: Impact, Charcoal, sans-serif;\n"
"letter-spacing: 2px;\n"
"word-spacing: 2px;\n"
"color: #000000;\n"
"font-weight: 400;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: normal;\n"
"text-transform: none;\n"
"color: rgb(0, 173, 188)")
        self.MatrX_text.setLineWidth(1)
        self.MatrX_text.setAlignment(QtCore.Qt.AlignCenter)
        self.MatrX_text.setWordWrap(False)
        self.MatrX_text.setObjectName("MatrX_text")
        self.myButton_2 = QtWidgets.QPushButton(Dialog)
        self.myButton_2.setEnabled(True)
        self.myButton_2.setGeometry(QtCore.QRect(275, 390, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.myButton_2.setFont(font)
        self.myButton_2.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.545, y2:1, stop:0 rgba(44, 104, 99, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    color: rgb(62, 255, 243);\n"
"    border: none;\n"
"    font-family: Impact, Charcoal, sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.511, y2:1, stop:0 rgba(72, 170, 162, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.myButton_2.setCheckable(False)
        self.myButton_2.setDefault(False)
        self.myButton_2.setFlat(False)
        self.myButton_2.setObjectName("myButton_2")
        self.cmd_lbl = QtWidgets.QLabel(Dialog)
        self.cmd_lbl.setGeometry(QtCore.QRect(135, 130, 370, 50))
        self.cmd_lbl.setStyleSheet("font-family: ABeeZee, sans-serif;\n"
"font-size: 20px;\n"
"font-weight: 100;\n"
"color: rgba(0, 221, 255, 1);\n"
"text-transform: none;\n"
"font-style: normal;\n"
"text-decoration: none;\n"
"line-height: 2em;\n"
"letter-spacing: 0px;")
        self.cmd_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.cmd_lbl.setObjectName("cmd_lbl")
        self.cmd_button = QtWidgets.QPushButton(Dialog)
        self.cmd_button.setEnabled(True)
        self.cmd_button.setGeometry(QtCore.QRect(260, 330, 120, 45))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.cmd_button.setFont(font)
        self.cmd_button.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.545, y2:1, stop:0 rgba(44, 104, 99, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    color: rgb(62, 255, 243);\n"
"    border: none;\n"
"    font-family: Impact, Charcoal, sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.511, y2:1, stop:0 rgba(72, 170, 162, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.cmd_button.setCheckable(False)
        self.cmd_button.setDefault(False)
        self.cmd_button.setFlat(False)
        self.cmd_button.setObjectName("cmd_button")
        self.minimize_button = QtWidgets.QPushButton(Dialog)
        self.minimize_button.setEnabled(True)
        self.minimize_button.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.minimize_button.setFont(font)
        self.minimize_button.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.545, y2:1, stop:0 rgba(44, 104, 99, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    color: rgb(62, 255, 243);\n"
"    border: none;\n"
"    font-family: Impact, Charcoal, sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.511, y2:1, stop:0 rgba(72, 170, 162, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.minimize_button.setCheckable(False)
        self.minimize_button.setDefault(False)
        self.minimize_button.setFlat(False)
        self.minimize_button.setObjectName("minimize_button")
        self.cmd_lineedit = QtWidgets.QLineEdit(Dialog)
        self.cmd_lineedit.setGeometry(QtCore.QRect(130, 170, 380, 40))
        self.cmd_lineedit.setStyleSheet("padding: 3px;\n"
"font-size: 22px;\n"
"border-width: 2px;\n"
"border-color: #41e1ff;\n"
"background-color: #000000;\n"
"color: #00f5ff;\n"
"border-style: groove;\n"
"border-radius: 0px;\n"
"box-shadow: 0px 0px 30px rgba(0,255,224,.95);\n"
"text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.cmd_lineedit.setObjectName("cmd_lineedit")
        self.OK_button = QtWidgets.QPushButton(Dialog)
        self.OK_button.setEnabled(True)
        self.OK_button.setGeometry(QtCore.QRect(290, 220, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.OK_button.setFont(font)
        self.OK_button.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.545, y2:1, stop:0 rgba(44, 104, 99, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    color: rgb(62, 255, 243);\n"
"    border: none;\n"
"    font-family: Impact, Charcoal, sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.511, y2:1, stop:0 rgba(72, 170, 162, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}\n"
"QPushButton:pressed {\n"
"    background:linear-gradient(to bottom, #000000 5%, #006285 100%);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.OK_button.setCheckable(False)
        self.OK_button.setDefault(False)
        self.OK_button.setFlat(False)
        self.OK_button.setObjectName("OK_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MatrX v0.0.2 Alpha"))
        self.label.setText(_translate("Dialog", "v.0.0.2 alpha"))
        self.myButton.setText(_translate("Dialog", "Start"))
        self.MatrX_text.setText(_translate("Dialog", "MatrX"))
        self.myButton_2.setText(_translate("Dialog", "Quite"))
        self.cmd_lbl.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">...</span></p></body></html>"))
        self.cmd_button.setText(_translate("Dialog", "Список команд"))
        self.minimize_button.setText(_translate("Dialog", "Minimize to tray"))
        self.OK_button.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
