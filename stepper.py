#!/usr/bin/env python
# coding: utf-8

# import libraries
import time
import RPi.GPIO as GPIO

# use BCM GPIO pin references
GPIO.setmode(GPIO.BCM)
# disable warnings
GPIO.setwarnings(False)
# set all pins as outputs
pins = [24,25,8,7]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)


class stepper():
    def __init__(self):
        self.numberSteps = 0
        self.stepCount = 0
        self.seq = []
        self.direction = 0
        self.stepCounter = 0

    def config(self, n, t, nb, d):
        if n == 4:
            # set number of steps per spin
            self.numberSteps = int(nb*(2048/360))
            # standard sequence (4 sec./spin)
            self.stepCount = 4
            self.seq = [i for i in range(0, self.stepCount)]
            self.seq[0] = [1,0,0,0]
            self.seq[1] = [0,1,0,0]
            self.seq[2] = [0,0,1,0]
            self.seq[3] = [0,0,0,1]
        
        elif n == 8:
            # set number of steps per spin
            self.numberSteps = int(nb*(4096/360))
            # advanced sequence (8 sec./spin)
            self.stepCount = 8
            self.seq = [i for i in range(0, self.stepCount)]
            self.seq[0] = [1,0,0,0]
            self.seq[1] = [1,1,0,0]
            self.seq[2] = [0,1,0,0]
            self.seq[3] = [0,1,1,0]
            self.seq[4] = [0,0,1,0]
            self.seq[5] = [0,0,1,1]
            self.seq[6] = [0,0,0,1]
            self.seq[7] = [1,0,0,1]
        
        self.direction = d
        self.waitTime = t

    def run(self):
        for i in range(self.numberSteps):
            for pin in range(4):
                xpin = pins[pin]
                if self.seq[self.stepCounter][pin] != 0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
            self.stepCounter += self.direction
            if (self.stepCounter == self.stepCount):
                self.stepCounter = 0
            if (self.stepCounter < 0):
                self.stepCounter = self.stepCount-1
            time.sleep(self.waitTime)


if __name__ == '__main__':
    #print("### STEPPER ###")
    try:
        s = stepper()
        # steps, time between steps, spin in degree, direction
        s.config(8, 0.002, 180, -1)
        
        while True:
            with open('i_status.txt', 'r') as f:
                i_status = f.read()
            f.close
            if i_status == "True":
                break
        print("Stepper - Received status")
        
        print("Stepper - Running")
        s.run()
        print("Stepper - Stopped")
        
    except KeyboardInterrupt:
        pass
    
    for pin in pins:
            GPIO.output(pin, False)
