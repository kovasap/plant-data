from datetime import datetime
import time

import click
import RPi.GPIO as GPIO
import pigpio

from . import gsheets
from . import sensors
from . import pigpio_dht11

@click.command()
@click.option(
    '--cadence', default=0,
    help='Time (in seconds) between measurements.  '
         'If 0, will take on measurement and then exit.')
def main(cadence):
    try:
        sheets_api = gsheets.GSheets()
        sensors.setup_distance()
        pi = pigpio.pi()
        temp_humidity_sensor = pigpio_dht11.DHT11(pi, 27)

        while True:
            try:
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
            except Exception as e:
                print(f'ERROR! {e}')
                time.sleep(60)
                continue
            if cadence == 0:
                break
            time.sleep(cadence)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
