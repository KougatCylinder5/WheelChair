import numpy
import cv2
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time

MoHat = Adafruit_MotorHAT(addr=0x60)

M3 = 3
M4 = 4

MotorLeft = MoHat.getMotor(M4)
MotorRight = MoHat.getMotor(M3)

motor_speed = 100

MotorLeft.setSpeed(motor_speed)
MotorRight.setSpeed(motor_speed)

print(MoHat.FORWARD)
MotorLeft.run(MoHat.FORWARD)
time.sleep(2.25)
MotorLeft.run(MoHat.RELEASE)