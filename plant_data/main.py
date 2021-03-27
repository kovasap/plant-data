import time

import RPi.GPIO as GPIO
import pigpio

import sensors
import pigpio_dht11


def main():
    try:
        sensors.setup_distance()
        pi = pigpio.pi()
        temp_humidity_sensor = pigpio_dht11.DHT11(pi, 27)

        while True:
            dist = sensors.calc_distance()
            th_read = temp_humidity_sensor.next()
            print(f'Temp: {th_read["temp_f"]:.1f} F / '
                  f'{th_read["temp_c"]:.1f} C   '
                  f'Humidity: {th_read["humidity"]}%')
            time.sleep(0.5)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
