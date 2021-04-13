from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox
import sys


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(470, 310, 271, 61))
        self.btnSave.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btnSave.setObjectName("btnSave")
        self.btnPump1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPump1.setGeometry(QtCore.QRect(470, 0, 151, 51))
        self.btnPump1.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btnPump1.setObjectName("btnPump1")
        self.btnPump2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPump2.setGeometry(QtCore.QRect(470, 60, 151, 51))
        self.btnPump2.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btnPump2.setObjectName("btnPump2")
        self.btnPump3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPump3.setGeometry(QtCore.QRect(470, 120, 151, 51))
        self.btnPump3.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btnPump3.setObjectName("btnPump3")
        self.btnPump4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnPump4.setGeometry(QtCore.QRect(470, 180, 151, 51))
        self.btnPump4.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btnPump4.setObjectName("btnPump4")
        self.lblTime_p1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTime_p1.setGeometry(QtCore.QRect(630, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTime_p1.setFont(font)
        self.lblTime_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime_p1.setObjectName("lblTime_p1")
        self.lblPulse_p1 = QtWidgets.QLabel(self.centralwidget)
        self.lblPulse_p1.setGeometry(QtCore.QRect(630, 30, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPulse_p1.setFont(font)
        self.lblPulse_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPulse_p1.setObjectName("lblPulse_p1")
        self.lblPulse_p2 = QtWidgets.QLabel(self.centralwidget)
        self.lblPulse_p2.setGeometry(QtCore.QRect(630, 80, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPulse_p2.setFont(font)
        self.lblPulse_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPulse_p2.setObjectName("lblPulse_p2")
        self.lblTime_p2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTime_p2.setGeometry(QtCore.QRect(630, 60, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTime_p2.setFont(font)
        self.lblTime_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime_p2.setObjectName("lblTime_p2")
        self.lblPulse_p3 = QtWidgets.QLabel(self.centralwidget)
        self.lblPulse_p3.setGeometry(QtCore.QRect(630, 150, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPulse_p3.setFont(font)
        self.lblPulse_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPulse_p3.setObjectName("lblPulse_p3")
        self.lblTime_p3 = QtWidgets.QLabel(self.centralwidget)
        self.lblTime_p3.setGeometry(QtCore.QRect(630, 130, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTime_p3.setFont(font)
        self.lblTime_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime_p3.setObjectName("lblTime_p3")
        self.lblPulse_p4 = QtWidgets.QLabel(self.centralwidget)
        self.lblPulse_p4.setGeometry(QtCore.QRect(630, 210, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPulse_p4.setFont(font)
        self.lblPulse_p4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPulse_p4.setObjectName("lblPulse_p4")
        self.lblTime_p4 = QtWidgets.QLabel(self.centralwidget)
        self.lblTime_p4.setGeometry(QtCore.QRect(630, 190, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTime_p4.setFont(font)
        self.lblTime_p4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime_p4.setObjectName("lblTime_p4")
        self.lblPulse = QtWidgets.QLabel(self.centralwidget)
        self.lblPulse.setGeometry(QtCore.QRect(20, 30, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPulse.setFont(font)
        self.lblPulse.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPulse.setObjectName("lblPulse")
        self.lblTime = QtWidgets.QLabel(self.centralwidget)
        self.lblTime.setGeometry(QtCore.QRect(20, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTime.setFont(font)
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 140, 191, 71))
        self.btn1.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btn1.setObjectName("btn1")
        self.txtbtn1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbtn1.setGeometry(QtCore.QRect(210, 160, 191, 41))
        self.txtbtn1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 31, 31,0.7);\n"
"font: 11pt \"Franklin Gothic Medium\";\n"
"border-radius: 15px;\n"
"background-size:10px;")
        self.txtbtn1.setText("")
        self.txtbtn1.setAlignment(QtCore.Qt.AlignCenter)
        self.txtbtn1.setPlaceholderText("")
        self.txtbtn1.setObjectName("txtbtn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(10, 220, 191, 71))
        self.btn2.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(10, 300, 191, 71))
        self.btn3.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btn3.setObjectName("btn3")
        self.txtbtn2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbtn2.setGeometry(QtCore.QRect(210, 240, 191, 41))
        self.txtbtn2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 31, 31,0.7);\n"
"font: 11pt \"Franklin Gothic Medium\";\n"
"border-radius: 15px;\n"
"background-size:10px;")
        self.txtbtn2.setText("")
        self.txtbtn2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtbtn2.setPlaceholderText("")
        self.txtbtn2.setObjectName("txtbtn2")
        self.txtbtn3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbtn3.setGeometry(QtCore.QRect(210, 320, 191, 41))
        self.txtbtn3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(31, 31, 31,0.7);\n"
"font: 11pt \"Franklin Gothic Medium\";\n"
"border-radius: 15px;\n"
"background-size:10px;")
        self.txtbtn3.setText("")
        self.txtbtn3.setAlignment(QtCore.Qt.AlignCenter)
        self.txtbtn3.setPlaceholderText("")
        self.txtbtn3.setObjectName("txtbtn3")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(470, 240, 271, 61))
        self.btnBack.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.btnBack.setObjectName("btnBack")
        self.rbTime = QtWidgets.QRadioButton(self.centralwidget)
        self.rbTime.setGeometry(QtCore.QRect(60, 63, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rbTime.setFont(font)
        self.rbTime.setObjectName("rbTime")
        self.rbPulse = QtWidgets.QRadioButton(self.centralwidget)
        self.rbPulse.setGeometry(QtCore.QRect(60, 90, 82, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rbPulse.setFont(font)
        self.rbPulse.setObjectName("rbPulse")
        self.frame_keyboard = QtWidgets.QFrame(self.centralwidget)
        self.frame_keyboard.setGeometry(QtCore.QRect(740, 40, 711, 251))
        self.frame_keyboard.setStyleSheet("background-color:rgba(0,0,0,0.0);")
        self.frame_keyboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_keyboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_keyboard.setObjectName("frame_keyboard")
        self.frame_5 = QtWidgets.QFrame(self.frame_keyboard)
        self.frame_5.setGeometry(QtCore.QRect(1, 70, 711, 181))
        self.frame_5.setStyleSheet("background-color: rgba(0,0,0,0.7);\n"
"border-radius: 25px;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.btnQ = QtWidgets.QPushButton(self.frame_5)
        self.btnQ.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.btnQ.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnQ.setObjectName("btnQ")
        self.btnEnter_2 = QtWidgets.QPushButton(self.frame_5)
        self.btnEnter_2.setGeometry(QtCore.QRect(640, 70, 61, 41))
        self.btnEnter_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnEnter_2.setObjectName("btnEnter_2")
        self.btnDelete_2 = QtWidgets.QPushButton(self.frame_5)
        self.btnDelete_2.setGeometry(QtCore.QRect(640, 120, 61, 41))
        self.btnDelete_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnDelete_2.setObjectName("btnDelete_2")
        self.btnW = QtWidgets.QPushButton(self.frame_5)
        self.btnW.setGeometry(QtCore.QRect(80, 20, 61, 41))
        self.btnW.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnW.setObjectName("btnW")
        self.btnE = QtWidgets.QPushButton(self.frame_5)
        self.btnE.setGeometry(QtCore.QRect(150, 20, 61, 41))
        self.btnE.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnE.setObjectName("btnE")
        self.btnR = QtWidgets.QPushButton(self.frame_5)
        self.btnR.setGeometry(QtCore.QRect(220, 20, 61, 41))
        self.btnR.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnR.setObjectName("btnR")
        self.btnT = QtWidgets.QPushButton(self.frame_5)
        self.btnT.setGeometry(QtCore.QRect(290, 20, 61, 41))
        self.btnT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnT.setObjectName("btnT")
        self.btnY = QtWidgets.QPushButton(self.frame_5)
        self.btnY.setGeometry(QtCore.QRect(360, 20, 61, 41))
        self.btnY.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnY.setObjectName("btnY")
        self.btnU = QtWidgets.QPushButton(self.frame_5)
        self.btnU.setGeometry(QtCore.QRect(430, 20, 61, 41))
        self.btnU.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnU.setObjectName("btnU")
        self.btnI = QtWidgets.QPushButton(self.frame_5)
        self.btnI.setGeometry(QtCore.QRect(500, 20, 61, 41))
        self.btnI.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnI.setObjectName("btnI")
        self.btnO = QtWidgets.QPushButton(self.frame_5)
        self.btnO.setGeometry(QtCore.QRect(570, 20, 61, 41))
        self.btnO.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnO.setObjectName("btnO")
        self.btnP = QtWidgets.QPushButton(self.frame_5)
        self.btnP.setGeometry(QtCore.QRect(640, 20, 61, 41))
        self.btnP.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnP.setObjectName("btnP")
        self.btnS = QtWidgets.QPushButton(self.frame_5)
        self.btnS.setGeometry(QtCore.QRect(80, 70, 61, 41))
        self.btnS.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnS.setObjectName("btnS")
        self.btnH = QtWidgets.QPushButton(self.frame_5)
        self.btnH.setGeometry(QtCore.QRect(360, 70, 61, 41))
        self.btnH.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnH.setObjectName("btnH")
        self.btnG = QtWidgets.QPushButton(self.frame_5)
        self.btnG.setGeometry(QtCore.QRect(290, 70, 61, 41))
        self.btnG.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnG.setObjectName("btnG")
        self.btnD = QtWidgets.QPushButton(self.frame_5)
        self.btnD.setGeometry(QtCore.QRect(150, 70, 61, 41))
        self.btnD.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnD.setObjectName("btnD")
        self.btnA = QtWidgets.QPushButton(self.frame_5)
        self.btnA.setGeometry(QtCore.QRect(10, 70, 61, 41))
        self.btnA.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnA.setObjectName("btnA")
        self.btnF = QtWidgets.QPushButton(self.frame_5)
        self.btnF.setGeometry(QtCore.QRect(220, 70, 61, 41))
        self.btnF.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnF.setObjectName("btnF")
        self.btnJ = QtWidgets.QPushButton(self.frame_5)
        self.btnJ.setGeometry(QtCore.QRect(430, 70, 61, 41))
        self.btnJ.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnJ.setObjectName("btnJ")
        self.btnK = QtWidgets.QPushButton(self.frame_5)
        self.btnK.setGeometry(QtCore.QRect(500, 70, 61, 41))
        self.btnK.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnK.setObjectName("btnK")
        self.btnL = QtWidgets.QPushButton(self.frame_5)
        self.btnL.setGeometry(QtCore.QRect(570, 70, 61, 41))
        self.btnL.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnL.setObjectName("btnL")
        self.btnN = QtWidgets.QPushButton(self.frame_5)
        self.btnN.setGeometry(QtCore.QRect(360, 120, 61, 41))
        self.btnN.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnN.setObjectName("btnN")
        self.btnC = QtWidgets.QPushButton(self.frame_5)
        self.btnC.setGeometry(QtCore.QRect(150, 120, 61, 41))
        self.btnC.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnC.setObjectName("btnC")
        self.btnZ = QtWidgets.QPushButton(self.frame_5)
        self.btnZ.setGeometry(QtCore.QRect(10, 120, 61, 41))
        self.btnZ.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnZ.setObjectName("btnZ")
        self.btnB = QtWidgets.QPushButton(self.frame_5)
        self.btnB.setGeometry(QtCore.QRect(290, 120, 61, 41))
        self.btnB.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnB.setObjectName("btnB")
        self.btnX = QtWidgets.QPushButton(self.frame_5)
        self.btnX.setGeometry(QtCore.QRect(80, 120, 61, 41))
        self.btnX.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnX.setObjectName("btnX")
        self.btnV = QtWidgets.QPushButton(self.frame_5)
        self.btnV.setGeometry(QtCore.QRect(220, 120, 61, 41))
        self.btnV.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnV.setObjectName("btnV")
        self.btnM = QtWidgets.QPushButton(self.frame_5)
        self.btnM.setGeometry(QtCore.QRect(430, 120, 61, 41))
        self.btnM.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnM.setObjectName("btnM")
        self.btnSpace = QtWidgets.QPushButton(self.frame_5)
        self.btnSpace.setGeometry(QtCore.QRect(500, 120, 131, 41))
        self.btnSpace.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnSpace.setObjectName("btnSpace")
        self.txtKeyboard_2 = QtWidgets.QLineEdit(self.frame_keyboard)
        self.txtKeyboard_2.setGeometry(QtCore.QRect(0, 20, 711, 41))
        self.txtKeyboard_2.setStyleSheet("background-color: rgb(60, 99, 98);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Franklin Gothic Heavy\";\n"
"border-radius: 15px;")
        self.txtKeyboard_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtKeyboard_2.setObjectName("txtKeyboard_2")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Calibration"))
        self.btnSave.setText(_translate("MainWindow", "SAVE"))
        self.btnPump1.setText(_translate("MainWindow", "Pump 1"))
        self.btnPump2.setText(_translate("MainWindow", "Pump 2"))
        self.btnPump3.setText(_translate("MainWindow", "Pump 3"))
        self.btnPump4.setText(_translate("MainWindow", "Pump 4"))
        self.lblTime_p1.setText(_translate("MainWindow", "TIME"))
        self.lblPulse_p1.setText(_translate("MainWindow", "PULSE"))
        self.lblPulse_p2.setText(_translate("MainWindow", "PULSE"))
        self.lblTime_p2.setText(_translate("MainWindow", "TIME"))
        self.lblPulse_p3.setText(_translate("MainWindow", "PULSE"))
        self.lblTime_p3.setText(_translate("MainWindow", "TIME"))
        self.lblPulse_p4.setText(_translate("MainWindow", "PULSE"))
        self.lblTime_p4.setText(_translate("MainWindow", "TIME"))
        self.lblPulse.setText(_translate("MainWindow", "PULSE"))
        self.lblTime.setText(_translate("MainWindow", "TIME"))
        self.btn1.setText(_translate("MainWindow", "Button1 "))
        self.btn2.setText(_translate("MainWindow", "Button 2"))
        self.btn3.setText(_translate("MainWindow", "Button3"))
        self.btnBack.setText(_translate("MainWindow", "BACK"))
        self.rbTime.setText(_translate("MainWindow", "Time"))
        self.rbPulse.setText(_translate("MainWindow", "Pulse"))
        self.btnQ.setText(_translate("MainWindow", "Q"))
        self.btnEnter_2.setText(_translate("MainWindow", "ENTER"))
        self.btnDelete_2.setText(_translate("MainWindow", "DELETE"))
        self.btnW.setText(_translate("MainWindow", "W"))
        self.btnE.setText(_translate("MainWindow", "E"))
        self.btnR.setText(_translate("MainWindow", "R"))
        self.btnT.setText(_translate("MainWindow", "T"))
        self.btnY.setText(_translate("MainWindow", "Y"))
        self.btnU.setText(_translate("MainWindow", "U"))
        self.btnI.setText(_translate("MainWindow", "I"))
        self.btnO.setText(_translate("MainWindow", "O"))
        self.btnP.setText(_translate("MainWindow", "P"))
        self.btnS.setText(_translate("MainWindow", "S"))
        self.btnH.setText(_translate("MainWindow", "H"))
        self.btnG.setText(_translate("MainWindow", "G"))
        self.btnD.setText(_translate("MainWindow", "D"))
        self.btnA.setText(_translate("MainWindow", "A"))
        self.btnF.setText(_translate("MainWindow", "F"))
        self.btnJ.setText(_translate("MainWindow", "J"))
        self.btnK.setText(_translate("MainWindow", "K"))
        self.btnL.setText(_translate("MainWindow", "L"))
        self.btnN.setText(_translate("MainWindow", "N"))
        self.btnC.setText(_translate("MainWindow", "C"))
        self.btnZ.setText(_translate("MainWindow", "Z"))
        self.btnB.setText(_translate("MainWindow", "B"))
        self.btnX.setText(_translate("MainWindow", "X"))
        self.btnV.setText(_translate("MainWindow", "V"))
        self.btnM.setText(_translate("MainWindow", "M"))
        self.btnSpace.setText(_translate("MainWindow", "SPACE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

