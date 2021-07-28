# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_List(object):
    def setupUi(self, List):
        List.setObjectName("List")
        List.resize(640, 480)
        List.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(List)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.label_2.setToolTipDuration(-1)
        self.label_2.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 103, 118, 255), stop:1 rgba(0, 0, 0, 255))")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(List)
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
        self.myButton = QtWidgets.QPushButton(List)
        self.myButton.setEnabled(True)
        self.myButton.setGeometry(QtCore.QRect(260, 360, 111, 51))
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
        self.MatrX_text = QtWidgets.QLabel(List)
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
        self.listWidget = QtWidgets.QListWidget(List)
        self.listWidget.setGeometry(QtCore.QRect(65, 130, 510, 190))
        self.listWidget.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"gridline-color: rgb(111, 255, 251);\n"
"font: 14pt \"SosTitle\";\n"
"color: rgb(60, 255, 242);")
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        _translate = QtCore.QCoreApplication.translate
        List.setWindowTitle(_translate("List", "Dialog"))
        self.label.setText(_translate("List", "v.0.0.2 alpha"))
        self.myButton.setText(_translate("List", "OK"))
        self.MatrX_text.setText(_translate("List", "MatrX"))


if __name__ == "__main__":
    import sys
    
