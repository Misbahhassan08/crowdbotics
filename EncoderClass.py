import pigpio
import time

class decoder:

   """Class to decode mechanical rotary encoder pulses."""

   def __init__(self, pi, gpioA, callback):
       self.pi = pi
       self.callback = callback
       self.gpioA = gpioA
       self.levA = 0
       self.count = 0
       self.pi.set_mode(gpioA, pigpio.INPUT)
       self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
       self.cbA = self.pi.callback(gpioA, pigpio.FALLING_EDGE, self._pulse)
 
   def _pulse(self, gpio, level, tick):
       self.count += 1
       t1 = self.pi.get_current_tick()
       self.callback(self.count, t1)
   def cancel(self):
      self.cbA.cancel()

