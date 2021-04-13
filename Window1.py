

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox
import sys


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.setEnabled(True)
        MainWindow.resize(771, 381)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 2, 511, 225))
        #self.graphicsView.setStyleSheet("background-image:url('Images/100.png')")
        self.graphicsView.setStyleSheet("\n"
                                        " \n"
                                        "background:rgba(0,0,0,0.0);\n"
                                        "background-image:url('Images/101.png');\n"
                                        "background-position: center;\n"
                                        "background-repeat: no-repeat;\n"
                                        
                                        )
        self.graphicsView.setObjectName("graphicsView")
        
        #self.frame_logo = QtWidgets.QFrame(self.centralwidget)
        #self.frame_logo.setGeometry(QtCore.QRect(0, 0, 511, 225))
        #self.frame_logo.setStyleSheet("background-color: rgb(170, 255, 255);")
        #self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.frame_logo.setObjectName("frame_logo")

        
        self.frame_output = QtWidgets.QFrame(self.centralwidget)
        self.frame_output.setGeometry(QtCore.QRect(509, -1, 261, 231))
        self.frame_output.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.frame_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_output.setObjectName("frame_output")
        self.label = QtWidgets.QLabel(self.frame_output)
        self.label.setGeometry(QtCore.QRect(50, 10, 171, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_output)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_output)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_output)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_output)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_output)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lbl_pump1 = QtWidgets.QLabel(self.frame_output)
        self.lbl_pump1.setGeometry(QtCore.QRect(90, 60, 181, 16))
        self.lbl_pump1.setObjectName("lbl_pump1")
        self.lbl_pump2 = QtWidgets.QLabel(self.frame_output)
        self.lbl_pump2.setGeometry(QtCore.QRect(90, 90, 181, 16))
        self.lbl_pump2.setObjectName("lbl_pump2")
        self.lbl_pump3 = QtWidgets.QLabel(self.frame_output)
        self.lbl_pump3.setGeometry(QtCore.QRect(90, 120, 181, 16))
        self.lbl_pump3.setObjectName("lbl_pump3")
        self.lbl_msg = QtWidgets.QLabel(self.frame_output)
        self.lbl_msg.setGeometry(QtCore.QRect(80, 160, 181, 20))
        self.lbl_msg.setObjectName("lbl_msg")
        self.lbl_error = QtWidgets.QLabel(self.frame_output)
        self.lbl_error.setGeometry(QtCore.QRect(70, 190, 191, 20))
        self.lbl_error.setObjectName("lbl_error")
        
        self.frame_selection = QtWidgets.QFrame(self.centralwidget)
        self.frame_selection.setGeometry(QtCore.QRect(0, 230, 511, 151))
        self.frame_selection.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.frame_selection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_selection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_selection.setObjectName("frame_selection")
        self.dial = QtWidgets.QDial(self.frame_selection)
        self.dial.setGeometry(QtCore.QRect(60, 40, 111, 111))
        self.dial.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 153, 129, 255), stop:1 rgba(255, 255, 255, 255));")
        self.dial.setMaximum(2)
        self.dial.setProperty("value", 1)
        self.dial.setSliderPosition(1)
        self.dial.setObjectName("dial")
        self.label_7 = QtWidgets.QLabel(self.frame_selection)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_selection)
        self.label_8.setGeometry(QtCore.QRect(100, 20, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_selection)
        self.label_9.setGeometry(QtCore.QRect(170, 120, 41, 16))
        self.label_9.setObjectName("label_9")


        self.cb_pump1 = QtWidgets.QCheckBox(self.frame_selection)
        self.cb_pump1.setGeometry(QtCore.QRect(420, 60, 81, 18))
        self.cb_pump1.setObjectName("cb_pump1")
        self.cb_pump2 = QtWidgets.QCheckBox(self.frame_selection)
        self.cb_pump2.setGeometry(QtCore.QRect(420, 90, 81, 18))
        self.cb_pump2.setObjectName("cb_pump2")
        self.cb_pump3 = QtWidgets.QCheckBox(self.frame_selection)
        self.cb_pump3.setGeometry(QtCore.QRect(420, 120, 81, 18))
        self.cb_pump3.setObjectName("cb_pump3")

        
        self.label_10 = QtWidgets.QLabel(self.frame_selection)
        self.label_10.setGeometry(QtCore.QRect(280, 10, 231, 31))
        self.label_10.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")

        self.label_27 = QtWidgets.QLabel(self.frame_selection)
        self.label_27.setGeometry(QtCore.QRect(200, 50, 181, 31))
        self.label_27.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_27.setObjectName("label_27")
        self.comboBox = QtWidgets.QComboBox(self.frame_selection)
        self.comboBox.setGeometry(QtCore.QRect(210, 80, 121, 22))
        self.comboBox.setObjectName("comboBox")

        
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(530, 250, 221, 51))
        self.btn_start.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 153, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btn_start.setObjectName("btn_start")
        self.btn_calibrate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calibrate.setGeometry(QtCore.QRect(530, 310, 221, 51))
        self.btn_calibrate.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 153, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btn_calibrate.setObjectName("btn_calibrate")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "STATUS/OUTPUT"))
        self.label_2.setText(_translate("MainWindow", "PUMP1 :"))
        self.label_3.setText(_translate("MainWindow", "PUMP2 :"))
        self.label_4.setText(_translate("MainWindow", "PUMP3 :"))
        self.label_5.setText(_translate("MainWindow", "TIME :"))
        self.label_6.setText(_translate("MainWindow", "ERROR:"))
        self.lbl_pump1.setText(_translate("MainWindow", "0.0"))
        self.lbl_pump2.setText(_translate("MainWindow", "0.0"))
        self.lbl_pump3.setText(_translate("MainWindow", "0.0"))
        self.lbl_msg.setText(_translate("MainWindow", "..."))
        self.lbl_error.setText(_translate("MainWindow", "..."))
        self.label_27.setText(_translate("MainWindow", "Select Oz/Ltl/ Gal"))
        self.label_7.setText(_translate("MainWindow", "LOW"))
        self.label_8.setText(_translate("MainWindow", "MID"))
        self.label_9.setText(_translate("MainWindow", "HIGH"))
        self.cb_pump1.setText(_translate("MainWindow", "Pump1"))
        self.cb_pump2.setText(_translate("MainWindow", "Pump2"))
        self.cb_pump3.setText(_translate("MainWindow", "Pump3"))
        self.label_10.setText(_translate("MainWindow", "Select Pumps"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_calibrate.setText(_translate("MainWindow", "Calibrate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
