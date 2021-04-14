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
import RPi.GPIO as GPIO
import threading
import sys
import sqlite3
from PyQt5.QtCore import QThread, pyqtSignal

        


class RPI(QThread):
    signalFlow = pyqtSignal(float, float, str,  name='m_signals')
    
    
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
        
        self.last_time1 = datetime.now()
        self.last_time2 = datetime.now()
        self.last_time3 = datetime.now()
        self.last_time4 = datetime.now()

        self.pump1Status = False
        self.pump2Status = False
        self.pump3Status = False
        self.pump4Status = False
        
        self.calibrate1 = False
        self.calibrate2 = False
        self.calibrate3 = False
        self.calibrate4 = False

        self.flow_rate1 = 0.0
        self.flow_rate2 = 0.0
        self.flow_rate3 = 0.0
        self.flow_rate4 = 0.0

        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        
        
        # Initiliaze all gpios as input and output
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pump1, GPIO.OUT)
        GPIO.setup(self.pump2, GPIO.OUT)
        GPIO.setup(self.pump3, GPIO.OUT)
        GPIO.setup(self.pump4, GPIO.OUT)
        
        GPIO.output(self.pump1, GPIO.LOW)
        GPIO.output(self.pump2, GPIO.LOW)
        GPIO.output(self.pump3, GPIO.LOW)
        GPIO.output(self.pump4, GPIO.LOW)
        
        #----------------------------------------------------------------------


        GPIO.setup(self.sensor1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.sensor1,GPIO.RISING,callback=self.pulseCallback1,bouncetime=20)

        GPIO.setup(self.sensor2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.sensor2,GPIO.RISING,callback=self.pulseCallback2,bouncetime=20)

        GPIO.setup(self.sensor3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.sensor3,GPIO.RISING,callback=self.pulseCallback3,bouncetime=20)

        GPIO.setup(self.sensor4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.sensor4,GPIO.RISING,callback=self.pulseCallback4,bouncetime=20)

        GPIO.setup(self.btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


        GPIO.setup(self.btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.ctime = datetime.now()

        print('INIT RPI DONE')
        self.deamon = True
        self.start()

    def stop(self):
        
        self.terminate()
        print("stop")
        
    def run(self):
        while True:
            #if (datetime.now() - self.ctime).total_seconds() > 1:
                #self.count1 = self.count1 + self.flow_rate1
                #self.count2 = self.count2 + self.flow_rate2
                #self.count3 = self.count3 + self.flow_rate3
                #self.count4 = self.count4 + self.flow_rate4
                #self.ctime = datetime.now()
            
            self.signalFlow.emit(int(self.count1),float(self.flow_rate1), 'pump1')
            self.signalFlow.emit(int(self.count2),float(self.flow_rate2), 'pump2')
            self.signalFlow.emit(int(self.count3),float(self.flow_rate3), 'pump3')
            self.signalFlow.emit(int(self.count4),float(self.flow_rate4), 'pump4')
            time.sleep(0.01)
            
            
            #print('{} , {}, {}'.format(self.count1,self.count2,self.count3))
            

    
    def pulseCallback1(self, p):
        self.count1 = self.count1 + 1

        current_time = datetime.now()
        diff = (current_time - self.last_time1).total_seconds()
       
        # Calculate current flow rate
        hertz = 1. / diff
        self.flow_rate1 = hertz / 7.5
       
        # Reset time of last pulse
        self.last_time1 = current_time

    
    
    
    def pulseCallback2(self, p):
        self.count2 = self.count2 + 1
        current_time = datetime.now()
        diff = (current_time - self.last_time2).total_seconds()
       
        # Calculate current flow rate
        hertz = 1. / diff
        self.flow_rate2 = hertz / 7.5
       
        # Reset time of last pulse
        self.last_time2 = current_time
    
    
    
    def pulseCallback3(self, p):
        self.count3 = self.count3 + 1
        # Calculate the time difference since last pulse recieved
        current_time = datetime.now()
        diff = (current_time - self.last_time3).total_seconds()
       
        # Calculate current flow rate
        hertz = 1. / diff
        self.flow_rate3 = hertz / 7.5
       
        # Reset time of last pulse
        self.last_time3 = current_time


    
    
    def pulseCallback4(self, p):
        self.count4 = self.count4 + 1 
        # Calculate the time difference since last pulse recieved
        current_time = datetime.now()
        diff = (current_time - self.last_time1).total_seconds()
       
        # Calculate current flow rate
        hertz = 1. / diff
        self.flow_rate4 = hertz / 7.5
       
        # Reset time of last pulse
        self.last_time4 = current_time
        

    def pump_1_on(self):
        GPIO.output(self.pump1, GPIO.HIGH)
        self. motor_status_1 = True
        
    def pump_2_on(self):
        GPIO.output(self.pump2, GPIO.HIGH)
        self. motor_status_2 = True

    def pump_3_on(self):
        GPIO.output(self.pump3, GPIO.HIGH)
        self. motor_status_3 = True

    def pump_4_on(self):
        GPIO.output(self.pump4, GPIO.HIGH)
        self. motor_status_4 = True

    def pump_1_off(self):
        GPIO.output(self.pump1, GPIO.LOW)
        self. motor_status_1 = False
        
    def pump_2_off(self):
        GPIO.output(self.pump2, GPIO.LOW)
        self. motor_status_2 = False

    def pump_3_off(self):
        GPIO.output(self.pump3, GPIO.LOW)
        self. motor_status_3 = False

    def pump_4_off(self):
        GPIO.output(self.pump4, GPIO.LOW)
        self. motor_status_4 = False


