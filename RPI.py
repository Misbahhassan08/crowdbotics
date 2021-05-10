"""
PUMP1 : GPIO 17
PUMP2 : GPIO 27
PUMP3 : GPIO 22
PUMP4 : GPIO 5

Sensor1 : GPIO 6
Sensor2 : GPIO 13
Sensor3 : GPIO 19
Sensor4 : GPIO 21

Button1 : GPIO 18
Button2 : GPIO 23
Button3 : GPIO 24
Button4 : GPIO 25

"""

import json
import time
from datetime import datetime
import pigpio
import threading
import sys
import sqlite3
from PyQt5.QtCore import QThread, pyqtSignal
from EncoderClass import decoder

        


class RPI(QThread):
    SensorFlow1 = pyqtSignal(int, float, name='m_signals1')
    SensorFlow2 = pyqtSignal(int, float, name='m_signals2')
    SensorFlow3 = pyqtSignal(int, float, name='m_signals3')
    SensorFlow4 = pyqtSignal(int, float, name='m_signals4')
    def __init__(self):
        QThread.__init__(self)
        # pumps Gpio's
        self.pump1 = 17
        self.pump2 = 27
        self.pump3 = 22
        self.pump4 = 5

        # Sensors Gpio's
        self.sensor1 = 6
        self.sensor2 = 13
        self.sensor3 = 19
        self.sensor4 = 21
        
        # Button Gpio
        self.btn1 = 18
        self.btn2 = 23
        self.btn3 = 24
        self.btn4 = 25

        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0

        self.tick1 = 0.0
        self.tick2 = 0.0
        self.tick3 = 0.0
        self.tick4 = 0.0

        self.pi = pigpio.pi()
        self.pi.set_mode(self.pump1, pigpio.OUTPUT)
        self.pi.set_mode(self.pump2, pigpio.OUTPUT)
        self.pi.set_mode(self.pump3, pigpio.OUTPUT)
        self.pi.set_mode(self.pump4, pigpio.OUTPUT)

        self.pi.write(self.pump1, 0)
        self.pi.write(self.pump2, 0)
        self.pi.write(self.pump3, 0)
        self.pi.write(self.pump4, 0)
        
        #----------------------------------------------------------------------
        self.s1 = decoder(self.pi,self.sensor1, self.callback1)
        self.s2 = decoder(self.pi,self.sensor2, self.callback2)
        self.s3 = decoder(self.pi,self.sensor3, self.callback3)
        self.s4 = decoder(self.pi,self.sensor4, self.callback4)
        self.b1 = decoder(self.pi,self.btn1, self.btnCallaback1)
        self.b2 = decoder(self.pi,self.btn2, self.btnCallaback2)
        self.b3 = decoder(self.pi,self.btn3, self.btnCallaback3)
        self.b4 = decoder(self.pi,self.btn4, self.btnCallaback4)
        time.sleep(0.01)
        print('INIT RPI DONE')

    def reset1(self):
        self.s1.count = 0.0
    def reset2(self):
        self.s2.count = 0.0
    def reset3(self):
        self.s3.count = 0.0
    def reset4(self):
        self.s4.count = 0.0

    def btnCallaback1(self, pulse, tick):
        pass
    def btnCallaback2(self, pulse, tick):
        pass
    def btnCallaback3(self, pulse, tick):
        pass
    def btnCallaback4(self, pulse, tick):
        pass
    
    def callback1(self, pulse, tick):
        self.count1 = pulse
        self.tick1 = tick
        self.SensorFlow1.emit(int(self.count1),float(self.tick1))
        
        pass
    
    def callback2(self, pulse, tick):
        self.count2 = pulse
        self.tick2= tick
        self.SensorFlow2.emit(int(self.count2),float(self.tick2))
        
        pass
    
    def callback3(self, pulse, tick):
        self.count3 = pulse
        self.tick3 = tick
        self.SensorFlow3.emit(int(self.count3),float(self.tick3))
        pass
    
    def callback4(self, pulse, tick):
        self.count4 = pulse
        self.tick4 = tick
        self.SensorFlow4.emit(int(self.count4),float(self.tick4))
        pass

    def pump_1_on(self):
        self.pi.write(self.pump1,1)
        
    def pump_2_on(self):
        self.pi.write(self.pump2,1)

    def pump_3_on(self):
        self.pi.write(self.pump3,1)

    def pump_4_on(self):
        self.pi.write(self.pump4,1)

    def pump_1_off(self):
        self.pi.write(self.pump1,0)
        
    def pump_2_off(self):
        self.pi.write(self.pump2,0)

    def pump_3_off(self):
        self.pi.write(self.pump3,0)

    def pump_4_off(self):
        self.pi.write(self.pump4,0)


