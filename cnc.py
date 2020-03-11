#!/usr/bin/python
# Dr Pi - 11/12/2019

from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
kit1 = MotorKit(address=0x61)

def X(Fsteps,Bsteps):

                for i in range(Fsteps):
                        kit1.stepper2.onestep(direction=stepper.FORWARD)

                for i in range(Bsteps):
                        kit1.stepper2.onestep(direction=stepper.BACKWARD)
                kit1.stepper2.release()

def Y(Fsteps, Bsteps):
                for i in range(Bsteps):
                        kit1.stepper1.onestep(direction=stepper.FORWARD)

                for i in range(Fsteps):
                        kit1.stepper1.onestep(direction=stepper.BACKWARD)
                kit1.stepper1.release()

# Jog #
# When function is called, pass X or Y to specify which Axis/Motor
# If Delta is given as +ve then run "Fsteps" (Forward Steps)
# If Delta is given as -ve then run "Bsteps" (Backward Steps)

def JOG(Axis, Delta):
        if Delta > 0:
                for x in range (0,20,1):
                        Axis(abs(Delta),0)
        elif Delta < 0:
                for x in range (0,20,1):
                        Axis(0,abs(Delta))

# LIF = Load Input File and Parse Gcode

def LIFR():
        filename = 'job.txt'
        with open(filename) as f:
                for line in f:
                        if "X" and "Y" in line:

                                Gx = (line.split(' ')[1])
                                Gx = (Gx[1:])
                                print(Gx)
                                JOG(X,int(Gx))
                                JOG(X,-int(Gx))

                                Gy = (line.split(' ')[2])
                                Gy = (Gy[1:])
                                print(Gy)
                                JOG(Y,int(Gy))
                                JOG(Y,-int(Gy))

LIFR()

exit()
