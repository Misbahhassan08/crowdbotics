
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



class GUI(QtWidgets.QWidget,threading.Thread):

    
    def __init__(self):
        threading.Thread.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.last_time1 = datetime.now()
        self.last_time2 = datetime.now()
        self.last_time3 = datetime.now()
        self.last_time4 = datetime.now()

        #thread loop crossing

        self.thread_loop = True

        self.mode = "Pulse" # Time
        
        self.rpi = RPI()
        self._screen1 = GUI1()
        self._screen2 = GUI2()

        self.screen1_message = ""
        self.screen1_error = ""

        self._screen2.frame_keyboard.setGeometry(QtCore.QRect(100,500,500,500))
        # rpi signals

        self.rpi.signalFlow.connect(self.flowrate)

        #btn_start, btn_calibrate, cb_pump1, cb_pump1,. lbl_pump1
        
        # ---------------------------    screen 1    --------------------------------------------------------------------------
        
        self._screen1.btn_s1_start.clicked.connect(lambda: self.btn_screen1_start())
        self._screen1.btn_s1_calibrate.clicked.connect(lambda: self.switch_to_screen2())
        self._screen1.cb_pump1.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump1))
        self._screen1.cb_pump2.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump2))
        self._screen1.cb_pump3.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump3))
        self._screen1.cb_pump4.toggled.connect(lambda: self.buttonState(self._screen1.cb_pump3))

        # ------------------------------  screen2   ---------------------------------------------------------------------------
        
        #self._screen2.btn_pump1.clicked.connect(lambda: self.screen2_pump1())
        #self._screen2.btn_pump2.clicked.connect(lambda: self.screen2_pump2())
        #self._screen2.btn_pump3.clicked.connect(lambda: self.screen2_pump3())
        
        self._screen2.btnBack.clicked.connect(lambda: self.btn_open_screen1())
        self._screen2.txtbtn1.mouseReleaseEvent = self.presstxt_btn1
        self._screen2.txtbtn2.mouseReleaseEvent = self.presstxt_btn2
        self._screen2.txtbtn3.mouseReleaseEvent = self.presstxt_btn3

        self._screen2.rbTime.toggled.connect(lambda:self.btnstate(self._screen2.rbTime))
        self._screen2.rbPulse.toggled.connect(lambda:self.btnstate(self._screen2.rbPulse))

        self._screen2.btn1.clicked.connect(lambda: self.btn1Clicked())
        self._screen2.btn2.clicked.connect(lambda: self.btn2Clicked())
        self._screen2.btn3.clicked.connect(lambda: self.btn3Clicked())

        
        
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

        self._screen2.btnA.clicked.connect(lambda: self.apress())
        self._screen2.btnB.clicked.connect(lambda: self.bpress())
        self._screen2.btnC.clicked.connect(lambda: self.cpress())
        self._screen2.btnD.clicked.connect(lambda: self.dpress())
        self._screen2.btnE.clicked.connect(lambda: self.epress())
        self._screen2.btnF.clicked.connect(lambda: self.fpress())
        self._screen2.btnG.clicked.connect(lambda: self.gpress())
        self._screen2.btnH.clicked.connect(lambda: self.hpress())
        self._screen2.btnI.clicked.connect(lambda: self.ipress())
        self._screen2.btnJ.clicked.connect(lambda: self.jpress())
        self._screen2.btnK.clicked.connect(lambda: self.kpress())
        self._screen2.btnL.clicked.connect(lambda: self.lpress())
        self._screen2.btnM.clicked.connect(lambda: self.mpress())
        self._screen2.btnN.clicked.connect(lambda: self.npress())
        self._screen2.btnO.clicked.connect(lambda: self.opress())
        self._screen2.btnP.clicked.connect(lambda: self.ppress())
        self._screen2.btnQ.clicked.connect(lambda: self.qpress())
        self._screen2.btnR.clicked.connect(lambda: self.rpress())
        self._screen2.btnS.clicked.connect(lambda: self.spress())
        self._screen2.btnT.clicked.connect(lambda: self.tpress())
        self._screen2.btnU.clicked.connect(lambda: self.upress())
        self._screen2.btnV.clicked.connect(lambda: self.vpress())
        self._screen2.btnW.clicked.connect(lambda: self.wpress())
        self._screen2.btnX.clicked.connect(lambda: self.xpress())
        self._screen2.btnY.clicked.connect(lambda: self.ypress())
        self._screen2.btnZ.clicked.connect(lambda: self.zpress())
        self._screen2.btnEnter_2.clicked.connect(lambda: self.enter_press())
        self._screen2.btnDelete_2.clicked.connect(lambda: self.delete_press())
        self._screen2.btnSpace.clicked.connect(lambda: self.space_press())
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
    def btn_screen1_start(self): # pressing start button
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
    def btn1Clicked(self):
        val = self._screen2.txtbtn1.text()
        if len(val)>0:
            self._screen2.btn1.setText(''+val)

    def btn2Clicked(self):
        val = self._screen2.txtbtn2.text()
        if len(val)>0:
            self._screen2.btn2.setText(''+val)
            
    def btn3Clicked(self):
        val = self._screen2.txtbtn3.text()
        if len(val)>0:
            self._screen2.btn3.setText(''+val)
            
    def btnstate(self,b):
        if b.text() == "Time":
            if b.isChecked() == True:
                print(b.text() + "is selected ")
                self.mode = "Time"
            else:
                print(b.text() + "is deSelectd")
        if b.text() == "Pulse":
            if b.isChecked() == True:
                print(b.text() + "is selected ")
                self.mode = "Pulse"
            else:
                print(b.text() + "is deSelectd")
        
        pass
    def presstxt_btn1(self, event):
        print('clicking')
        self._screen2.frame_keyboard.setGeometry(QtCore.QRect(10,60,711,251))
        self.kb = 1
        pass
    def presstxt_btn2(self, event):
        print('clicking')
        self._screen2.frame_keyboard.setGeometry(QtCore.QRect(10,60,711,251))
        self.kb = 2
        pass
    def presstxt_btn3(self, event):
        print('clicking')
        self._screen2.frame_keyboard.setGeometry(QtCore.QRect(10,60,711,251))
        self.kb = 3
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
    def apress(self):
        print('pressing a')
        self.txtUpdate('A')

    def bpress(self):
        print('pressing b')
        self.txtUpdate('B')

    def cpress(self):
        print('pressing c')
        self.txtUpdate('C')

    def dpress(self):
        print('pressing d')
        self.txtUpdate('D')

    def epress(self):
        print('pressing e')
        self.txtUpdate('E')

    def fpress(self):
        print('pressing f')
        self.txtUpdate('F')

    def gpress(self):
        print('pressing g')
        self.txtUpdate('G')

    def hpress(self):
        print('pressing h')
        self.txtUpdate('H')

    def ipress(self):
        print('pressing i')
        self.txtUpdate('I')

    def jpress(self):
        print('pressing j')
        self.txtUpdate('J')

    def kpress(self):
        print('pressing k')
        self.txtUpdate('K')

    def lpress(self):
        print('pressing l')
        self.txtUpdate('L')

    def mpress(self):
        print('pressing m')
        self.txtUpdate('M')

    def npress(self):
        print('pressing n')
        self.txtUpdate('N')

    def opress(self):
        print('pressing o')
        self.txtUpdate('O')

    def ppress(self):
        print('pressing p')
        self.txtUpdate('P')

    def qpress(self):
        print('pressing q')
        self.txtUpdate('Q')

    def rpress(self):
        print('pressing r')
        self.txtUpdate('R')

    def spress(self):
        print('pressing s')
        self.txtUpdate('S')

    def tpress(self):
        print('pressing t')
        self.txtUpdate('T')

    def upress(self):
        print('pressing u')
        self.txtUpdate('U')

    def vpress(self):
        print('pressing v')
        self.txtUpdate('V')

    def wpress(self):
        print('pressing w')
        self.txtUpdate('W')

    def xpress(self):
        print('pressing x')
        self.txtUpdate('X')

    def ypress(self):
        print('pressing y')
        self.txtUpdate('Y')

    def zpress(self):
        print('pressing z')
        self.txtUpdate('Z')

    def enter_press(self):
        print('pressing enter')
        mesg = '{}'.format(self._screen2.txtKeyboard_2.text())
        if self.kb == 1:
            self._screen2.txtbtn1.setText(mesg)
            pass
        elif self.kb == 2:
            self._screen2.txtbtn2.setText(mesg)
            pass
        elif self.kb == 3:
            self._screen2.txtbtn3.setText(mesg)
            pass
        
        
        self._screen2.txtKeyboard_2.setText('')
        self._screen2.frame_keyboard.setGeometry(QtCore.QRect(630, 640, 711, 251))
        self.kb = 0

    def delete_press(self):
        print('pressing delete')
        # deleting last character
        self.txtdelete()

    def space_press(self):
        print('pressing space')
        # nothing happen actually
        pass
    
    def txtUpdate(self, txt):
        lent = len(self._screen2.txtKeyboard_2.text())
        if len(self._screen2.txtKeyboard_2.text()) == 0:
            self._screen2.txtKeyboard_2.setText('{}'.format(txt))
        else:
            v = self._screen2.txtKeyboard_2.text()
            self._screen2.txtKeyboard_2.setText('{}{}'.format(v, txt))

    def txtdelete(self):
        vr = self._screen2.txtKeyboard_2.text()
        vrnew = ''
        lr_length = len(vr) - 1
        i = 0;
        for str in vr:
            if i == lr_length:
                pass
            else:
                vrnew = '{}{}'.format(vrnew, str)
            i += 1
        print(vrnew)
        self._screen2.txtKeyboard_2.setText(vrnew)

    def run(self):
        
        #main loop function
        self.thread_loop = True
        while self.thread_loop:
            #print(self.i)
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
    

    
