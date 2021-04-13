
import json
import time
from datetime import datetime, time
import threading
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
from screen1 import Ui_MainWindow1
from screen2 import Ui_MainWindow2

from RPI import RPI


    
def clickable(widget: object) -> object:
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget and event.type() == QEvent.MouseButtonRelease and obj.rect().contains(event.pos()):
                self.clicked.emit()
                return True
            else:
                return False
def clickable2(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
                    return False
            filter = Filter(widget)
            widget.installEventFilter(filter)
            return filter.clicked

class GUI1(QtWidgets.QWidget,Ui_MainWindow1 ):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
        print('INIT: GUI1')
        pass

class GUI2(QtWidgets.QWidget,Ui_MainWindow2 ):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        print('INIT: GUI2')
        #self.pushButton_2.clicked.connect(lambda: self._motor4())
        pass



class GUI(threading.Thread):

    
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.last_time1 = datetime.now()
        self.last_time2 = datetime.now()
        self.last_time3 = datetime.now()
        self.last_time4 = datetime.now()

        #thread loop crossing

        self.thread_loop = True
        
        self.rpi = RPI()
        self._screen1 = GUI1()
        self._screen2 = GUI2()

        self.screen1_message = ""
        self.screen1_error = ""

        self._screen2.frame_keyboard.setGeometry(QtCore.QRect(100,500,500,500))
        # rpi signals

        self.rpi.signalFlow.connect(self.flowrate)

        #btn_start, btn_calibrate, cb_pump1, cb_pump1,. lbl_pump1
        # screen 1 
        self._screen1.btn_s1_start.clicked.connect(lambda: self.btn_screen1_start())
        self._screen1.btn_s1_calibrate.clicked.connect(lambda: self.switch_to_screen2())
        self._screen1.cb_pump1.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump1))
        self._screen1.cb_pump2.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump2))
        self._screen1.cb_pump3.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump3))
        self._screen1.cb_pump4.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump3))

        # screen2
        #self._screen2.btn_pump1.clicked.connect(lambda: self.screen2_pump1())
        #self._screen2.btn_pump2.clicked.connect(lambda: self.screen2_pump2())
        #self._screen2.btn_pump3.clicked.connect(lambda: self.screen2_pump3())
        
        self._screen2.btnBack.clicked.connect(lambda: self.btn_open_screen1())

        clickable2(self._screen2.txtbtn1).connect(self.presstxt_btn1())

        self.s1BtnStart = False
        self.screen1 = True
        self.screen2 = False

        self.kb = 0 # keyboard position value 0 = hide, 1= btn1 active, 2= btn2 actve 3= btn3 active
        self.motor1 = False
        self.motor2 = False
        self.motor3 = False
        self.motor4 = False

        self.pump1_hz = 0
        self.pump2_hz = 0
        self.pump3_hz = 0
        self.pump4_hz = 0

        self.flow_rate1 = 0.0
        self.flow_rate2 = 0.0
        self.flow_rate3 = 0.0
        self.flow_rate4 = 0.0


        self.i =0 # show screen 1
        #self.i =1 # check screen 1 is open 
        #self.i =2 #show screen 2
        #self.i =3 # check screen 2 is open
        #self.i =4 #show screen 3
        #self.i =5 # check screen 3 is open
        self._screen1.show()
        self._screen2.show()
        
        self.i = 1
        self._screen2.hide()
       

        self.start()
        pass

    
    #************************ Signals *******************************************
    
            
    def flowrate(self, val ,val2 ,p):
        if p == "pump1":
            self.pump1_hz = val
            self.flow_rate1 = val2
            pass
        elif p == "pump2":
            self.pump2_hz = val
            self.flow_rate2 = val2
            pass
        elif p == "pump3":
            self.pump3_hz = val
            self.flow_rate3 = val2
            pass
        elif p == "pump4":
            self.pump4_hz = val
            self.flow_rate4 = val2
            pass
        pass

    

    def buttonState(self, b):
        
        try:
        
            if True:
                if b.text() == "Pump1":
                    if b.isChecked():
                        self.motor1 = True
                    else:
                        self.motor1 = False
                        self.screen1_message = "Pump1 UnSelect"
                            
                elif b.text() == "Pump2":
                    if b.isChecked():
                        self.motor2 = True
                    else:
                        self.motor2 = False
                        self.screen1_message = "Pump2 UnSelect"
                            
                elif b.text() == "Pump3":
                    if b.isChecked():
                        self.motor3 = True
                    else:
                        self.motor3 = False
                        self.screen1_message = "Pump3 UnSelect"

                elif b.text() == "Pump4":
                    if b.isChecked():
                        self.motor4 = True
                    else:
                        self.motor4 = False
                        self.screen1_message = "Pump4 UnSelect"
                            
                pass
            pass
        except Exception as error:
            self.screen1_error="Error {}".format(error)
        
        pass
    def stop(self):
        self.thread_loop = False
        self.join()


    #------------------------------------------ Screen 1 Functions --------------------------------------------------------------------------
    def btn_screen1_start(): # pressing start button
        if self.s1BtnStart:
            self.s1BtnStart = False
        else:
            self.s1BtnStart = True 
        pass
    
    def switch_to_screen2(self):
        self.screen2 = True
        self.screen1 = False
        self.i = 2
        self.motor1 = False
        self.motor2 = False
        self.motor3 = False
        self.motor4 = False
        pass
    #------------------------------------- Screen 2 Functions --------------------------------------------------------------------------------
    def presstxt_btn1(self):
        self._screen2.frame_keyboard.setGeometry(QtCore.QRect(10,60,711,251))
        pass
    def btn_open_screen1(self):
        self.screen2 = False
        self.screen1 = True
        self.i = 0
        self.motor1 = False
        self.motor2 = False
        self.motor3 = False
        self.motor4 = False
        pass

    def run(self):
        
        #main loop function
        self.thread_loop = True
        while self.thread_loop:
            print(self.i)
            #print('GUI is running')
            a = datetime.now()
            seconds = a.second
            minut = a.minute
            hour = a.hour
            
            timestamp1 = str(datetime.now())
            if self.screen1:
                if self.i == 0:
                    print('SHOW SCREEN1')
                    self._screen1.show()
                    self._screen2.hide()
                    self.i = 1
                #print('In Screen 1')
                self._screen1.lbl_pump1.setText('{},{}Hz'.format(self.pump1_hz, int(self.flow_rate1)))
                self._screen1.lbl_pump2.setText('{},{}Hz'.format(self.pump2_hz, int(self.flow_rate2)))
                self._screen1.lbl_pump3.setText('{},{}Hz'.format(self.pump3_hz, int(self.flow_rate3)))
                self._screen1.lbl_pump4.setText('{},{}Hz'.format(self.pump4_hz, int(self.flow_rate4)))
               
                if self.s1BtnStart == False:
                    #nothing happen clieck to start
                    self._screen1.btn_s1_start.setText('Start')
                    self.rpi.count1 = 0.0
                    self.rpi.count2 = 0.0
                    self.rpi.count3 = 0.0
                    self.rpi.count4 = 0.0
                    self.rpi.pump_1_off()
                    self.rpi.pump_2_off()
                    self.rpi.pump_3_off()
                    self.rpi.pump_4_off()
                    pass
                else:
                    self._screen1.btn_s1_start.setText('Stop')
                    if self.motor1:
                        pass
                        
                    if self.motor2:
                        pass
                        
                    if self.motor3:
                        pass
                        
                    if self.motor4:
                        pass
               
                pass
            elif self.screen2:
                #print('In screen 2')
                if self.i == 2:
                    print('SHOW SCREEN2')
                    self._screen2.show()
                    self._screen1.hide()
                    
                    self.i = 3
                    
                else:
                    
                    a = datetime.now()
                    seconds = a.second
                    minut = a.minute
                    hour = a.hour
                    #self._screen2.lbl_time.setText('{}:{}:{}'.format(hour,minut,seconds))
                    

                    if self.motor1:
                        self.rpi.pump_1_on()
                        self.rpi.pump_2_off()
                        self.rpi.pump_3_off()
                        self.rpi.pump_4_off()
                        
                        pass
                    elif self.motor2:
                        self.rpi.pump_1_off()
                        self.rpi.pump_2_on()
                        self.rpi.pump_3_off()
                        self.rpi.pump_4_off()
                        
                        pass
                    elif self.motor3:
                        self.rpi.pump_1_off()
                        self.rpi.pump_2_off()
                        self.rpi.pump_3_on()
                        self.rpi.pump_4_off()
                        
                        pass
                    else:
                        self.rpi.pump_1_off()
                        self.rpi.pump_2_off()
                        self.rpi.pump_3_off()
                        self.rpi.pump_4_off()
                        self.rpi.count1 = 0.0
                        self.rpi.count2 = 0.0
                        self.rpi.count3 = 0.0
                        self.rpi.count4 = 0.0          
                pass
        print('Loop ended')


def main():

    
    app = QtWidgets.QApplication(sys.argv)
    project = GUI()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    
    main()
    pass
    

    
