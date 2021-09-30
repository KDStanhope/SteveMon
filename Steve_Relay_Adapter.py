##################################################
#    CH1 ---- 5 (BCM)
#    CH2 ---- 6 (BCM)
#    CH3 ---- 13 (BCM)
#    CH4 ---- 16 (BCM)
#    CH5 ---- 19 (BCM)
#    CH6 ---- 20 (BCM)
#    CH7 ---- 21 (BCM)
#    CH8 ---- 26 (BCM)
##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

class Relay:
    """Relay object"""
    def __init__(self, channel):
        if channel == 1:
            self.channel = channel
            self.bcm_channel = 5
        elif channel == 2:
            self.channel = channel
            self.bcm_channel = 6
        elif channel == 3:
            self.channel = channel
            self.bcm_channel = 13
        elif channel == 4:
            self.channel = channel
            self.bcm_channel = 16

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bcm_channel,GPIO.OUT)


    def on(self):
        GPIO.output(self.bcm_channel,GPIO.LOW)
        return True

    def off(self):
        GPIO.output(self.bcm_channel,GPIO.HIGH)
        return False

    def status(self):
        if GPIO.input(self.bcm_channel) == 0:
            return True
        else:
            return False
        
    def reset_all():
        GPIO.cleanup()