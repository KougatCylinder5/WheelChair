import numpy
import cv2
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time
import gpiozero

MoHat = Adafruit_MotorHAT(addr=0x60)

M3 = 3
M4 = 4

MotorLeft = MoHat.getMotor(M4)
MotorRight = MoHat.getMotor(M3)

motor_speed = 100

MotorLeft.setSpeed(motor_speed)
MotorRight.setSpeed(motor_speed)

MotorLeft.run(MoHat.FORWARD)
MotorRight.run(MoHat.FORWARD)
time.sleep(2)
MotorLeft.run(MoHat.RELEASE)
MotorRight.run(MoHat.RELEASE)

