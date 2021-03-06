#!/usr/bin/python3

# Taken from https://pimylifeup.com/raspberry-pi-distance-sensor/
# and https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/

import time

# Using this old deprecated library might not be necessary after
# https://github.com/adafruit/Adafruit_CircuitPython_DHT/issues/49 is fixed.
# Using the old library on my RPi4 requires this hack:
# https://stackoverflow.com/questions/63232072/cannot-import-name-beaglebone-black-driver-from-adafruit-dht/63311551#63311551
import Adafruit_DHT
import adafruit_dht
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

def calc_distance():
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


# ------------------- Temperature/Humidity ---------------------------------

# Temperature/humidity sensor GPIO numbers.
TEMP_DATA_PIN = board.D27

def setup_temp_humidity():
    return adafruit_dht.DHT11(TEMP_DATA_PIN, use_pulseio=False)

def calc_temp_humidity(dht_dev):
    try:
        # Print the values to the serial port
        humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 27)
        # temp_c = dht_dev.temperature
        temp_f = temp_c * (9 / 5) + 32
        # humidity = dht_dev.humidity
        print(f'Temp: {temp_f:.1f} F / {temp_c:.1f} C   Humidity: {humidity}%')
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        dht_dev.exit()
        raise error


# ------------------- Main Loop ---------------------------------

try:
    setup_distance()
    dhtDevice = setup_temp_humidity()

    while True:
        calc_distance()
        calc_temp_humidity(dhtDevice)
        time.sleep(0.5)
finally:
    GPIO.cleanup()
