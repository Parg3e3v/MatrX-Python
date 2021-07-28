# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Update(object):
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
        self.myButton.setGeometry(QtCore.QRect(265, 320, 110, 50))
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
        self.MatrX_text_2 = QtWidgets.QLabel(Dialog)
        self.MatrX_text_2.setGeometry(QtCore.QRect(240, 190, 160, 60))
        self.MatrX_text_2.setMinimumSize(QtCore.QSize(0, 0))
        self.MatrX_text_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
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
"color: rgb(69, 240, 255)")
        self.MatrX_text_2.setLineWidth(1)
        self.MatrX_text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.MatrX_text_2.setWordWrap(False)
        self.MatrX_text_2.setObjectName("MatrX_text_2")
        self.MatrX_text_3 = QtWidgets.QLabel(Dialog)
        self.MatrX_text_3.setGeometry(QtCore.QRect(20, 250, 611, 60))
        self.MatrX_text_3.setMinimumSize(QtCore.QSize(0, 0))
        self.MatrX_text_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
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
"color:rgb(15, 191, 255)")
        self.MatrX_text_3.setLineWidth(1)
        self.MatrX_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.MatrX_text_3.setWordWrap(False)
        self.MatrX_text_3.setObjectName("MatrX_text_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "v.0.0.2 alpha"))
        self.myButton.setText(_translate("Dialog", "Update"))
        self.MatrX_text.setText(_translate("Dialog", "MatrX"))
        self.MatrX_text_2.setText(_translate("Dialog", "Update Avilable"))
        self.MatrX_text_3.setText(_translate("Dialog", "Если программа не будет обновлена, то она не будет запускатся. \n"
"Это сделано в целях предотвращения багаюзерства"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Update()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
