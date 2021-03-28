# Plant Data Management Utilities

## Periodic Picture Taking

Add this line
```
0 * * * * ~/plant-data/take_picture.bash
```
to `crontab -u pi -e`.  This takes a picture every hour.

Useful references:

 - https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md


## Temperature and Humidity Sensing

Uses `pigpio`, which requires you to start a daemon with `sudo pigpiod` to
work.

Add this line (or whatever corresponds to your poetry virtualenv created by
`poetry shell`).
```
0 * * * * /home/pi/.cache/pypoetry/virtualenvs/plant-data-nC_HxkvU-py3.7/bin/plant-data
```
to `crontab -u pi -e`.  This takes a measurement every hour.


## Google Sheets Integration

Need to follow
https://denisluiz.medium.com/python-with-google-sheets-service-account-step-by-step-8f74c26ed28e
to set things up properly (see also
https://github.com/juampynr/google-spreadsheet-reader).
