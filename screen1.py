from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox
import sys


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_s1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_s1.setGeometry(QtCore.QRect(0, 0, 761, 371))
        self.frame_s1.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.frame_s1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_s1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_s1.setObjectName("frame_s1")
        self.frame_s1_selection = QtWidgets.QFrame(self.frame_s1)
        self.frame_s1_selection.setGeometry(QtCore.QRect(0, 230, 511, 151))
        self.frame_s1_selection.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.frame_s1_selection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_s1_selection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_s1_selection.setObjectName("frame_s1_selection")
        self.btn1 = QtWidgets.QPushButton(self.frame_s1_selection)
        self.btn1.setGeometry(QtCore.QRect(10, 20, 141, 51))
        self.btn1.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.frame_s1_selection)
        self.btn2.setGeometry(QtCore.QRect(190, 20, 141, 51))
        self.btn2.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.frame_s1_selection)
        self.btn3.setGeometry(QtCore.QRect(360, 20, 141, 51))
        self.btn3.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btn3.setObjectName("btn3")
        self.btn_s1_start = QtWidgets.QPushButton(self.frame_s1)
        self.btn_s1_start.setGeometry(QtCore.QRect(530, 260, 221, 51))
        self.btn_s1_start.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 153, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btn_s1_start.setObjectName("btn_s1_start")
        self.btn_s1_calibrate = QtWidgets.QPushButton(self.frame_s1)
        self.btn_s1_calibrate.setGeometry(QtCore.QRect(530, 310, 221, 51))
        self.btn_s1_calibrate.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 153, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btn_s1_calibrate.setObjectName("btn_s1_calibrate")
        self.frame_s1_output = QtWidgets.QFrame(self.frame_s1)
        self.frame_s1_output.setGeometry(QtCore.QRect(509, -1, 261, 191))
        self.frame_s1_output.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.frame_s1_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_s1_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_s1_output.setObjectName("frame_s1_output")
        self.label = QtWidgets.QLabel(self.frame_s1_output)
        self.label.setGeometry(QtCore.QRect(50, 40, 171, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_s1_output)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_s1_output)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_s1_output)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_s1_output)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 71, 21))
        self.label_5.setObjectName("label_5")
        self.lbl_pump1 = QtWidgets.QLabel(self.frame_s1_output)
        self.lbl_pump1.setGeometry(QtCore.QRect(90, 70, 161, 16))
        self.lbl_pump1.setObjectName("lbl_pump1")
        self.lbl_pump2 = QtWidgets.QLabel(self.frame_s1_output)
        self.lbl_pump2.setGeometry(QtCore.QRect(90, 90, 161, 16))
        self.lbl_pump2.setObjectName("lbl_pump2")
        self.lbl_pump3 = QtWidgets.QLabel(self.frame_s1_output)
        self.lbl_pump3.setGeometry(QtCore.QRect(90, 110, 161, 16))
        self.lbl_pump3.setObjectName("lbl_pump3")
        self.lbl_msg = QtWidgets.QLabel(self.frame_s1_output)
        self.lbl_msg.setGeometry(QtCore.QRect(80, 160, 320, 21))
        self.lbl_msg.setObjectName("lbl_msg")
        self.label_6 = QtWidgets.QLabel(self.frame_s1_output)
        self.label_6.setGeometry(QtCore.QRect(70, 10, 101, 31))
        self.label_6.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(200, 0, 3);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame_s1_output)
        self.label_11.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_11.setObjectName("label_11")
        self.lbl_pump4 = QtWidgets.QLabel(self.frame_s1_output)
        self.lbl_pump4.setGeometry(QtCore.QRect(90, 130, 161, 16))
        self.lbl_pump4.setObjectName("lbl_pump4")
        self.frame_logo = QtWidgets.QFrame(self.frame_s1)
        self.frame_logo.setGeometry(QtCore.QRect(0, 0, 511, 225))
        self.frame_logo.setStyleSheet("\n"
                                        " \n"
                                        "background:rgba(0,0,0,0.0);\n"
                                        "background-image:url('Images/101.png');\n"
                                        "background-position: center;\n"
                                        "background-repeat: no-repeat;\n")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.cb_pump1 = QtWidgets.QCheckBox(self.frame_s1)
        self.cb_pump1.setGeometry(QtCore.QRect(530, 200, 91, 18))
        self.cb_pump1.setObjectName("cb_pump1")
        self.cb_pump4 = QtWidgets.QCheckBox(self.frame_s1)
        self.cb_pump4.setGeometry(QtCore.QRect(660, 230, 91, 18))
        self.cb_pump4.setObjectName("cb_pump4")
        self.cb_pump3 = QtWidgets.QCheckBox(self.frame_s1)
        self.cb_pump3.setGeometry(QtCore.QRect(660, 200, 91, 18))
        self.cb_pump3.setObjectName("cb_pump3")
        self.cb_pump2 = QtWidgets.QCheckBox(self.frame_s1)
        self.cb_pump2.setGeometry(QtCore.QRect(530, 230, 91, 18))
        self.cb_pump2.setObjectName("cb_pump2")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "Button1 "))
        self.btn2.setText(_translate("MainWindow", "Button1 "))
        self.btn3.setText(_translate("MainWindow", "Button1 "))
        self.btn_s1_start.setText(_translate("MainWindow", "Start"))
        self.btn_s1_calibrate.setText(_translate("MainWindow", "Calibrate"))
        self.label.setText(_translate("MainWindow", "STATUS/OUTPUT"))
        self.label_2.setText(_translate("MainWindow", "PUMP1 :"))
        self.label_3.setText(_translate("MainWindow", "PUMP2 :"))
        self.label_4.setText(_translate("MainWindow", "PUMP3 :"))
        self.label_5.setText(_translate("MainWindow", "Message:"))
        self.lbl_pump1.setText(_translate("MainWindow", "0/200"))
        self.lbl_pump2.setText(_translate("MainWindow", "0/200"))
        self.lbl_pump3.setText(_translate("MainWindow", "0/200"))
        self.lbl_msg.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "Version 3.0"))
        self.label_11.setText(_translate("MainWindow", "PUMP4 :"))
        self.lbl_pump4.setText(_translate("MainWindow", "0/200"))
        self.cb_pump1.setText(_translate("MainWindow", "Pump1"))
        self.cb_pump4.setText(_translate("MainWindow", "Pump4"))
        self.cb_pump3.setText(_translate("MainWindow", "Pump3"))
        self.cb_pump2.setText(_translate("MainWindow", "Pump2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
