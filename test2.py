import json
import time
import threading
import sys

from datetime import datetime
import pigpio
from RPI import RPI

pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0

t1 = 0.0
t2 = 0.0
t3 = 0.0
t4 = 0.0

rpi = RPI()
pi = pigpio.pi()
def flowrate1(p,t):
    global pos1
    global t1
    pos1 = p
    t1 = t
    print("call flow rate 1")
    pass
def flowrate2(p,t):
    global pos2
    global t2
    pos2 = p
    t2 = t
    print("call flow rate 2")
    pass




time_new = pi.get_current_tick() + (1000000 * 15)
rpi.pump_1_on()
rpi.pump_2_on()
while pi.get_current_tick() <= time_new:
    #rpi.SensorFlow1.connect(flowrate1)
    #rpi.SensorFlow2.connect(flowrate2)
    print("Sensor1 : {} with tick {} , Sensor2 :{} with tick {}".format(rpi.count1,rpi.tick1,rpi.count2,rpi.tick2))
    pass
rpi.pump_1_off()
rpi.pump_2_off()

