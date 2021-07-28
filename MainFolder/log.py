# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Log(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.label_2.setToolTipDuration(-1)
        self.label_2.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 103, 118, 255), stop:1 rgba(0, 0, 0, 255))")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QLineEdit(Dialog)
        self.login.setGeometry(QtCore.QRect(130, 170, 381, 41))
        self.login.setStyleSheet("padding: 3px;\n"
"font-size: 22px;\n"
"border-width: 2px;\n"
"border-color: #41e1ff;\n"
"background-color: #000000;\n"
"color: #00f5ff;\n"
"border-style: groove;\n"
"border-radius: 0px;\n"
"box-shadow: 0px 0px 30px rgba(0,255,224,.95);\n"
"text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.login.setObjectName("login")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 100, 121, 16))
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
        self.myButton.setGeometry(QtCore.QRect(260, 340, 111, 51))
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
        self.MatrX_text.setGeometry(QtCore.QRect(0, 0, 641, 131))
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
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(130, 240, 381, 41))
        self.password.setStyleSheet("padding: 3px;\n"
"font-size: 22px;\n"
"border-width: 2px;\n"
"border-color: #41e1ff;\n"
"background-color: #000000;\n"
"color: #00f5ff;\n"
"border-style: groove;\n"
"border-radius: 0px;\n"
"box-shadow: 0px 0px 30px rgba(0,255,224,.95);\n"
"text-shadow: 0px 0px 5px rgba(66,66,66,.75);")
        self.password.setText("")
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.MatrX_text_2 = QtWidgets.QLabel(Dialog)
        self.MatrX_text_2.setGeometry(QtCore.QRect(0, 160, 181, 61))
        self.MatrX_text_2.setMinimumSize(QtCore.QSize(0, 0))
        self.MatrX_text_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.MatrX_text_2.setFont(font)
        self.MatrX_text_2.setMouseTracking(False)
        self.MatrX_text_2.setStyleSheet("font-family: Impact, Charcoal, sans-serif;\n"
"letter-spacing: 2px;\n"
"word-spacing: 2px;\n"
"color: #000000;\n"
"font-weight: 400;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: normal;\n"
"text-transform: none;\n"
"color: rgb(0, 173, 188)")
        self.MatrX_text_2.setLineWidth(1)
        self.MatrX_text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.MatrX_text_2.setWordWrap(False)
        self.MatrX_text_2.setObjectName("MatrX_text_2")
        self.MatrX_text_3 = QtWidgets.QLabel(Dialog)
        self.MatrX_text_3.setGeometry(QtCore.QRect(-20, 230, 181, 61))
        self.MatrX_text_3.setMinimumSize(QtCore.QSize(0, 0))
        self.MatrX_text_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.MatrX_text_3.setFont(font)
        self.MatrX_text_3.setMouseTracking(False)
        self.MatrX_text_3.setStyleSheet("font-family: Impact, Charcoal, sans-serif;\n"
"letter-spacing: 2px;\n"
"word-spacing: 2px;\n"
"color: #000000;\n"
"font-weight: 400;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: normal;\n"
"text-transform: none;\n"
"color: rgb(0, 173, 188)")
        self.MatrX_text_3.setLineWidth(1)
        self.MatrX_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.MatrX_text_3.setWordWrap(False)
        self.MatrX_text_3.setObjectName("MatrX_text_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 120, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font-family: Impact, Charcoal, sans-serif;\n"
"letter-spacing: 2px;\n"
"word-spacing: 2px;\n"
"color: #000000;\n"
"font-weight: 400;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: normal;\n"
"text-transform: none;\n"
"color: rgb(58, 255, 249)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.error = QtWidgets.QLabel(Dialog)
        self.error.setGeometry(QtCore.QRect(160, 280, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.error.setFont(font)
        self.error.setAutoFillBackground(False)
        self.error.setStyleSheet("font-family: Impact, Charcoal, sans-serif;\n"
"letter-spacing: 2px;\n"
"word-spacing: 2px;\n"
"color: #000000;\n"
"font-weight: 400;\n"
"text-decoration: none;\n"
"font-style: normal;\n"
"font-variant: normal;\n"
"text-transform: none;\n"
"color: rgb(60, 187, 255)")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "v.0.0.1 alpha"))
        self.myButton.setText(_translate("Dialog", "OK"))
        self.MatrX_text.setText(_translate("Dialog", "MatrX"))
        self.MatrX_text_2.setText(_translate("Dialog", "Login"))
        self.MatrX_text_3.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Log in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Log()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
