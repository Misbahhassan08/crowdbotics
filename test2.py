import json
import time
from datetime import datetime
from RPI import RPI 


rpi = RPI()

rpi.pump_1_on()
time.sleep(3)
rpi.pump_1_off()

