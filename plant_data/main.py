from datetime import datetime
import time

import RPi.GPIO as GPIO
import pigpio

import gsheets
import sensors
import pigpio_dht11


def main():
    try:
        sheets_api = gsheets.GSheets()
        sensors.setup_distance()
        pi = pigpio.pi()
        temp_humidity_sensor = pigpio_dht11.DHT11(pi, 27)

        while True:
            dist = sensors.calc_distance()
            th_read = temp_humidity_sensor.next()
            sheets_api.append_row([[
                datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                th_read['temp_f'],
                th_read['humidity'],
                dist,
            ]])
            print(f'Temp: {th_read["temp_f"]:.1f} F / '
                  f'{th_read["temp_c"]:.1f} C   '
                  f'Humidity: {th_read["humidity"]}%')
            time.sleep(10 * 60)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
