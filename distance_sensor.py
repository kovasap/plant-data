#!/usr/bin/python

# Taken from https://pimylifeup.com/raspberry-pi-distance-sensor/

from __future__ import print_function

import RPi.GPIO as GPIO
import time

GPIO.cleanup()
try:
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print('Waiting for sensor to settle...')
    time.sleep(2)

    while True:
        print('Calculating distance...', end='')
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
              pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
              pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time

        # Ultrasonic sound moves at 34300 cm/s, and our sound must move twice
        # the distance to the object (there and back).
        distance = round(pulse_duration * 17150, 2)
        print(distance, ' cm')
        time.sleep(0.5)
finally:
    GPIO.cleanup()
