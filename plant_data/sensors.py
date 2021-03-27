#!/usr/bin/python3

# Taken from https://pimylifeup.com/raspberry-pi-distance-sensor/
# and https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/

import time
from typing import Tuple

# Using this old deprecated library might not be necessary after
# https://github.com/adafruit/Adafruit_CircuitPython_DHT/issues/49 is fixed.
# Using the old library on my RPi4 requires this hack:
# https://stackoverflow.com/questions/63232072/cannot-import-name-beaglebone-black-driver-from-adafruit-dht/63311551#63311551
# import Adafruit_DHT
# import adafruit_dht
import board
import RPi.GPIO as GPIO


# ------------------- Distance ---------------------------------

# Distance sensor GPIO numbers.
DIST_TRIGGER_PIN = 4
DIST_ECHO_PIN = 17

def setup_distance():
    GPIO.setup(DIST_TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(DIST_ECHO_PIN, GPIO.IN)

    GPIO.output(DIST_TRIGGER_PIN, GPIO.LOW)
    print('Waiting for sensor to settle...')
    time.sleep(2)

def calc_distance() -> float:
    """Returns distance in cm."""
    print('Calculating distance...', end='')
    GPIO.output(DIST_TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(DIST_TRIGGER_PIN, GPIO.LOW)

    while GPIO.input(DIST_ECHO_PIN)==0:
          pulse_start_time = time.time()
    while GPIO.input(DIST_ECHO_PIN)==1:
          pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time

    # Ultrasonic sound moves at 34300 cm/s, and our sound must move twice
    # the distance to the object (there and back).
    distance = round(pulse_duration * 17150, 2)
    print(distance, ' cm')
    return distance


# ------------------- Temperature/Humidity ---------------------------------

# TODO delete this old adafruit library using code.
def calc_temp_humidity() -> Tuple[float, float, float]:
    """Returns temp in F, temp in C, and percent humidity."""
    try:
        # Print the values to the serial port
        # humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 27)
        temp_f = temp_c * (9 / 5) + 32
        print(f'Temp: {temp_f:.1f} F / {temp_c:.1f} C   Humidity: {humidity}%')
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        raise error
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        raise error
    return temp_f, temp_c, humidity


# ------------------- Main Loop ---------------------------------

def main():
    try:
        setup_distance()

        while True:
            dist = calc_distance()
            time.sleep(0.5)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
